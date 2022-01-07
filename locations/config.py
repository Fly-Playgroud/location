class Baidu:
    KEY = "E5iotyTZUq8QZVwZTK59MvExQHwcyhnH"
    OUTPUT = "JSON"  # 定义返回的数据类型：JSON or XML


class Amap:
    KEY = "856e640a5711908e3a5a7c4029fbb465"
    OUTPUT = "JSON"  # 定义返回的数据类型：JSON or XML


config = {
    "amap": Amap,
    "baidu": Baidu,
}
