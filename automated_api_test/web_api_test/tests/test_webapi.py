import pytest

from automated_api_test.web_api_test.src.Base_API_Page import WebApiPage


@pytest.fixture(scope="module")
def api_setup():
    base_url = "https://www.kurtosys.com"
    return WebApiPage(base_url)


def test_api_status_code(api_setup):
    response = api_setup.get_response("/")
    assert response.status_code == 200, "Status code is not 200"


def test_response_time(api_setup):
    response = api_setup.get_response("/")
    assert response.elapsed.total_seconds() < 2, "Response time is more than 2 seconds"


def test_server_header(api_setup):
    response = api_setup.get_response("/")
    assert response.headers.get("Server") == "Cloudflare", "Server header is not Cloudflare"
