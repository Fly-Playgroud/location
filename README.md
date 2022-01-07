## Introduction

对百度地图和高德地图的 地理编码API 进行封装。可以用于地理位置的经纬度获取。

## Usage

`config.py` 修改为开放平台的key

```python
class Baidu:
    KEY = ""
    OUTPUT = "JSON"  # 定义返回的数据类型：JSON or XML


class Amap:
    KEY = ""
    OUTPUT = "JSON"  # 定义返回的数据类型：JSON or XML


config = {
    "amap": Amap,
    "baidu": Baidu,
}
```

**Example**

- `locator`可选参数：
  - `ampap` 使用高德地图
  - `baidu` 使用百度地图 
- `address` 查询地址

```python
from locations import create_location
app = create_location(locator="amap")
app.locate(address="山东省")
```