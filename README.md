# nuwe-cimiss-python

中国气象局 CIMISS 数据库 MUSIC 接口的 python API。

## 安装

使用如下命令安装`nuwe_cimiss`包。

```
python setup.py install
```

## 开始使用

MUSIC 接口仅适用于气象局内网用户，使用前请先申请账户。

使用 `nuwe_cimiss.CimissClient` 类从 CIMISS 中检索数据。

需要提供 CIMISS 服务的相关参数，可以保存在当前目录 `client.conf` 文件中，
或者在创建 `nuwe_cimiss.CimissClient` 对象显式指定。参数包括：

- `music_server`: MUSIC接口ip地址，必须指定
- `music_port`：MUSIC接口端口号，必须指定
- `music_connTimeout`：连接超时，秒，可选
- `music_readTimeout`：数据读取超时，秒，可选
- `music_ServiceId`：默认服务节点id

下面的示例展示如何检索地面观测资料。

```python
from nuwe_cimiss import CimissClient

client_config_path="path/to/client/config/file"
user="user name"
password="user password"
server_id = "server id"

interface_id = "getSurfEleByTimeRange"

params = {
    "dataCode": "SURF_CHN_MUL_HOR",
    "elements": "Station_Id_d,Lat,Lon,Alti,Day,Hour,PRS_Sea,TEM,"
    "DPT,WIN_D_INST,WIN_S_INST,PRE_1h,PRE_6h,PRE_24h,PRS",
    "timeRange": "[20190817000000,20190817020000)",
    "orderby": "Station_ID_d:ASC",
    "limitCnt": "10",
}

client = CimissClient(
    user=user,
    password=password,
    config_file=client_config_path
)
result = client.callAPI_to_array2D(interface_id, params)
```

更详细的接口使用方法请访问 CIMISS 官网。

## 示例

请访问 `example` 目录查看示例。

## 移植 music-sdk-python-2.0.0

**music-sdk-python-2.0.0** 版权属于**国家气象信息中心**。
因软件包中未明确列出版权协议，本项目目前包含对该源码的修改。
如有侵权，请联系perillaroc或发issue声明。

本项目的`music-sdk-python-2.0.0`目录是对该版本的不完整修改，
从 Python 2 移植到 Python 3，使用 Requests 替换 pyCURL 库，并支持 Windows 和 Linux。

### 移植到 Python 3

Python 2 将于 2019 年底停止维护，所以还是需要开发基于 Python 3 的访问库。
本项目移植的内容包括：

- 为浮点数除法添加显式类型转换（`float`）
- 使用 `io.StringIO` 代替 `StringIO.StringIO`
- 使用 `io.BytesIO` 代替 `StringIO`
- 使用 `urllib.request.urlopen` 代替 `urllib2.urlopen`
- 使用 `configparser` 代替 `ConfigParser`
- 使用 `int` 代替 `string.stoi`
- 修改 `print` 语句

详细的代码改动请参考：[commit ad7cff8c](https://github.com/perillaroc/cimiss-python-api/commit/ad7cff8cc2bc443713e39f96b184912241a430b9)

### 使用 Requests 代替 pyCURL

pyCURL 比 Request 速度更快，但更多情况下，速度的快慢取决于网速和服务器的速度，另外 pyCURL 在 Windows 下使用不太方便，
所以使用更简单的 Requests 更有利于开发和维护。

## License

`nuwe-cimiss-api` 未做特殊声明部分代码由 perillaroc 开发，并采用 MIT 协议。

其中，**music-sdk-python-2.0.0** 版权属于**国家气象信息中心**。
