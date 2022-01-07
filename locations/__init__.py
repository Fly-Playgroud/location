from .import config
from .import location


def create_location(locator="amap"):
    app = location.Location(config.config.get(locator))
    return app
