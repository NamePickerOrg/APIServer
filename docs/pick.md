## NamePicker API Server API文档 抽选部分

### /pick/{name_list}

在指定名单中抽选

请求方法 `GET`
> 除了name_list项在URL处填写，其他参数均使用
>
> /pick/example?xxx=yyy
>
> 的形式赋值

|性别偏好|学号偏好|对应值|
|---|---|---|
|都抽|都抽|-1|
|只抽男|只抽单数|0|
|只抽女|只抽双数|1|
|只抽特殊性别|/|2|

|参数|描述|是否必填？|默认值|类型|
|---|---|---|---|---|
|name_list|抽选名单|是|无|字符串|
|sex_favor|性别偏好|否|-1|整数|
|num_favor|学号偏好|否|-1|整数|
|allow_repeat|是否允许重复|否|false|布尔值|
|num|抽选数量|否|1|整数|

#### 200 OK
返回样例：
```json
{
    "result":[
        {"name":"HKS","sex":1,"no":1},
        {"name":"sunxiaochuan","sex":2,"no":3}
    ]
}
```

#### 404 Not Found

##### 为什么？
在你提供的筛选条件内，没有符合条件的学生

返回样例：
```json
{"detail":"Not Found"}
```

#### 422 Unprocessable Entity

##### 为什么？
你提供了非法的参数

输入样例：
```
/pick/test2?sex_favor=miaowu
```

返回样例：
```json
{
    "detail":[
        {
            "type":"int_parsing",
            "loc":["query","sex_favor"],
            "msg":"Input should be a valid integer, unable to parse string as an integer",
            "input":"miaowu"
        }
    ]
}
```