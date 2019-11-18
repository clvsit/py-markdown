# Markdown 接口文档
一个简单的 markdown 文档生成工具包。

【支持内容】：
- 各级标题：h1、h2、h3、h4、h5；
- 列表：无序列表和有序列表；
- 链接
- 图片
- 表格
- 代码块

## Quick start
该工具包支持两种形式创建 markdown 文档。若您是面向对象开发的忠实拥趸，或是对面向对象开发有着深厚经验，推荐使用面向对象的方式来创建 markdown 文档。

【示例：面向对象】：
```python
md = Markdown()
md.set_h1("Markdown 接口文档")
md.set_content("一个简单的 markdown 文档生成工具包。")
md.write("Markdown.md", is_cover=False)
```

除了上述方式外，该工具包还支持基于配置的创建方式。用户可以将配置信息填写在 JSON 文件或者是 YAML 文件中，然后将其导入到 Markdown 对象，即可创建 markdown 文档。

【示例：基于配置项】：
- 编写配置文件，以 JSON 文件为例。

```json
[
    {"type": "h1", "content": "Markdown 接口文档"}，
    {"type": "content", "content": "一个简单的 markdown 文档生成工具包。"
]
```
- 编写脚本文件。

```python
with open("XXX.json", "r", encoding="utf-8") as file:
    config = json.load(file)
    md = Markdown(config)
    md.write("Markdown.md", is_cover=False)
```

基于配置项的方式适合于创建 markdown 文档模板，对于内容较多的情况，推荐使用面向对象的编程方式。

## 初始化
【语法】：
```python
Markdown(config=None)
```
config：可以传入配置文件的路径，也可以直接传入配置项字典。

【示例】：
```
# 传入 JSON 配置文件
md = Markdown("md_config.json")

# 传入 YAML 配置文件
md = Markdown("md_config.yaml")

# 传入配置项字典
md_config = {
    {"type": "h1", "content": "Markdown 接口文档"}，
    {"type": "content", "content": "一个简单的 markdown 文档生成工具包。"
}
md = Markdown(md_config)
```



## API 说明

### add_h*(title)
通过指定 \* 号不同的数字，可以添加 markdown 对应等级标题，例如 add\_h1(title) 添加一级标题，add\_h2(title) 添加二级标题。

\* 号可以取 1、2、3、4、5 这 5 个整数。

#### 函数说明
```python
add_h1(title)
add_h2(title)
add_h3(title)
add_h4(title)
add_h5(title)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
title | 标题内容 | str | 是 | 标题的内容

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 title 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_h1("Markdown 接口文档")
md.add_h2("API 说明")
md.add_h3("set_h*(title)")
md.add_h4("使用示例")
```

### add_h(title, level)
添加 markdown 的各级标题，是 set\_h*() 方法的整合写法。

#### 函数说明
```python
add_h(title, level="h2")
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
title | 标题内容 | str | 是 | 标题的内容
level | 标题等级 | str | 否 | 默认为 "h2"，可填写的内容为"h1"、"h2"、"h3"、"h4"、"h5"

【注意】：当 level 参数传入的值不符合参数列表中的要求时，默认设置为 "h2"。

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 title 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_h("Markdown 接口文档", level="h1")
```

### add_content()
添加正文内容。

#### 函数说明
```python
add_content(content, is_wrap=True)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
content | 正文内容 | str | 是 | 需要添加的文本内容
is_wrap | 是否换行 | bool | 否 | 默认为 True，即在当前文本的末尾加上 "\n"

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 content 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_h("set_content()", level="h3")
md.add_content("添加正文内容。")
```

### add_content()
添加正文内容。

#### 函数说明
```python
add_content(content, is_wrap=True)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
content | 正文内容 | str | 是 | 需要添加的文本内容
is_wrap | 是否换行 | bool | 否 | 默认为 True，即在当前文本的末尾加上 "\n"

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 content 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_h("set_content()", level="h3")
md.add_content("添加正文内容。")
```

### add_list()
添加列表，Markdown 的列表共有两种类型：有序列表以及无序列表。

#### 函数说明
```python
add_list(content_dict)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
content_dict | 列表信息对象 | dict | 是 | 包含列表相关信息的字典

【content_dict 示例】：
```python
{
    "style": "ol",
    "content": [
        "有序列表1",
        "有序列表2",
        {
            "style": "ul",
            "content": [
                "无序列表1",
                "无序列表2"
            ]
        }
    ]
}
```
上述 content_dict 代码对应的效果如下：
1. 有序列表1
2. 有序列表2
    - 无序列表1
    - 无序列表2

通过指定 style 的值来确定使用有序列表（ol）还是无序列表（ul）。通过嵌套 content 的形式来实现嵌套的列表形式，同一个 content 下的内容为同一级。 

【注意】：若不提高 style 值，则默认设置为无序列表。

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 content_dict 参数不为字典类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_h("set_content()", level="h3")
md.add_content("添加正文内容。")
md.add_list({
    "style": "ol",
    "content": [
        "有序列表1",
        "有序列表2",
        {
            "style": "ul",
            "content": [
                "无序列表1",
                "无序列表2"
            ]
        }
    ]
})
```


### add_image()
添加图片内容。

#### 函数说明
```python
add_image(image_path, image_text)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
image_path | 图片地址 | str | 是 | 添加图片的 URL 地址
image_text | 图片内容 | str | 否 | 默认为“无”，用户可自行添加有关图片的描述文本

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 image\_path 和 image\_text 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_image()
```


### add_link()
添加网页链接。

#### 函数说明
```python
add_link(link_path, link_text)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
link_path | 链接地址 | str | 是 | 链接对应的 URL 地址
link_text | 链接内容 | str | 否 | 默认为“链接内容”，用户可自行添加链接要显示的描述文本

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 link\_path 和 link\_text 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_image()
```


### add_code()
添加代码区域。

#### 函数说明
```python
add_code(code_content, code_type)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
code_content | 代码内容 | str | 是 | 需要添加的代码块内容
code_type | 代码类型 | str | 是 | 代码块的语言类型，部分 Markdown 编辑器能够识别语言类型并对代码进行高亮显示

code\_content 参数传入的代码块内容需自行进行换行，若代码较多，则推荐使用 """ 将代码块包裹后传入 `add_code()` 函数中。

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 code\_content 和 code\_type 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_image()
```


### add_table()
添加代码区域。

#### 函数说明
```python
add_table(table_info, data)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
table_info | 表格信息字典 | dict | 是 | 包含如何设置表格的信息
data | 表格数据 | iter | 是 | 可迭代对象，包含需要显示的所有表格数据

【table_info 示例】：
```
# index：数字
{
    "参数名": {"align": "left", "index": 0},
    "中文名": {"align": "left", "index": 1},
    "数据类型": {"align": "left", "index": 2},
    "是否必选": {"align": "center", "index": 3},
    "描述": {"align": "left", "index": 4}
}

# index：字符串
{
    "参数名": {"align": "left", "index": "name"},
    "中文名": {"align": "left", "index": "chinese"},
    "数据类型": {"align": "left", "index": "type"},
    "是否必选": {"align": "center", "index": "is_must"},
    "描述": {"align": "left", "index": "desc"}
}
```
- 表格信息字典中的 key 代表要显示的表头名称。
- align：表示对齐方式。
    - left：左对齐
    - center：居中对齐
    - right：右对齐
- index：用于指定 data（表格数据）中哪些数据用以填充当前列。index 可以是数字，也可以是具体的 key 名称，这取决于 data 的数据类型。

【data 示例】：
```python
# List of List
[
    ["table_info", "表格信息字典", "dict", "是", "..."],
    ["data", "表格数据", "iter", "是", "..."],
]
# List of dict
[
    {"name": "table_info", "chinese": "表格信息字典", "type": "dict", "is_must": "是", "desc": "..."],
    ["name": "data", "chinese": "表格数据", "type": "iter", "is_must": "是", "desc": "..."],
]
```

#### 返回内容
Markdown 对象。

#### 报错内容
- TypeError：当传入的 table\_info 参数不为字典类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_image()
```

### add_wrap()
添加换行符。

#### 函数说明
```python
add_wrap()
```

#### 返回内容
Markdown 对象

#### 使用示例
```python
md = Markdown()
md.add_h1("Markdown 接口文档")
md.add_wrap()
md.add_h2("API　说明")
md.write("Markdown 接口文档.md", is_cover=False)
```


### write()
生成 markdown 文件。

#### 函数说明
```python
write(output_path, is_cover)
```

#### 参数列表

参数名 | 中文名 | 数据类型 | 是否必选 | 描述
---|---|---|:---:|---
output_path | 导出路径 | str | 是 | markdown 文件的导出路径
is_cover | 是否覆盖 | bool | 否 | 默认为 False，即不覆盖

#### 返回内容
None

#### 报错内容
- TypeError：当传入的 output\_path 参数不为字符串类型时，引发该错误。

#### 使用示例
```python
md = Markdown()
md.add_h1("Markdown 接口文档")
md.write("Markdown 接口文档.md", is_cover=False)
```
