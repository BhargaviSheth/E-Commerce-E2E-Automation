import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="Choose browser: chrome or firefox"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("--browser_name").lower()  # Normalize case

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--disable-notifications")  # Example additional options
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)

    else:
        raise ValueError("Unsupported browser! Use --browser_name=chrome or --browser_name=firefox")

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver  # Provide the driver to the test function

    driver.quit()  # Ensure proper cleanup


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)