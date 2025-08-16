## NamePicker API Server API文档 基础部分

###  /

获取Hello World信息

请求方法 `GET`

#### 200 OK
返回样例：
```json
{"resp":"Hello World"}
```

#### 正常情况下，不存在非200返回

----

### /version

获取服务端版本

请求方法 `GET`

#### 200 OK
返回样例：
```json
{
    "version":"NamePicker API Server v0.0.1", // 完整版本号
    "codename":"Elysia", // 开发代号
    "protocol":"v1" // 协议版本号
}
```

#### 正常情况下，不存在非200返回

