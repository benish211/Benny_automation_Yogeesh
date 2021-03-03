import pytest
from Configuration.driver_factory import DriverFactory

@pytest.fixture()
def setup(request):
    driver=DriverFactory.get_driver("chrome")
    driver.implicitly_wait(10)
    request.cls.driver=driver
    before_failed=request.session.testsfailed
    yield
    if request.session.testsfailed!=before_failed:
        print("failed error")
    driver.quit()
