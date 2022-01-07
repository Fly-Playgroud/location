from .import config
from .import location


def creat_location(locator="amap"):
    app = location.Location(config.config.get(locator))
    return app
