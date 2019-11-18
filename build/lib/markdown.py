class Markdown:

    def __init__(self):
        self.content_ = ""

    def add_h(self, title: str, level: str = "h2") -> "Markdown":
        """
        添加 h 标题
        :param title: str 标题内容
        :param level: str 标题等级
        :return: Markdown 对象
        """
        if type(title) != str:
            raise TypeError("The param title must be str!")

        level_dict = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5}
        num = level_dict[level] if level in level_dict else 2

        self.content_ += "{level} {title}\n".format_map({
            "level": "#" * num,
            "title": title
        })
        return self

    def add_h1(self, title: str) -> "Markdown":
        """
        添加 h1 标题
        :param title: str 标题内容
        :return: Markdown 对象
        """
        if type(title) != str:
            raise TypeError("The param title must be str!")

        self.content_ += "# {title}\n".format(title=title)
        return self

    def add_h2(self, title: str) -> "Markdown":
        """
        添加 h2 标题
        :param title: str 标题内容
        :return: Markdown 对象
        """
        if type(title) != str:
            raise TypeError("The param title must be str!")

        self.content_ += "## {title}\n".format(title=title)
        return self

    def add_h3(self, title: str) -> "Markdown":
        """
        添加 h3 标题
        :param title: str 标题内容
        :return: Markdown 对象
        """
        if type(title) != str:
            raise TypeError("The param title must be str!")

        self.content_ += "### {title}\n".format(title=title)
        return self

    def add_h4(self, title: str) -> "Markdown":
        """
        添加 h4 标题
        :param title: str 标题内容
        :return: Markdown 对象
        """
        if type(title) != str:
            raise TypeError("The param title must be str!")

        self.content_ += "#### {title}\n".format(title=title)
        return self

    def add_h5(self, title: str) -> "Markdown":
        """
        添加 h5 标题
        :param title: str 标题内容
        :return: Markdown 对象
        """
        if type(title) != str:
            raise TypeError("The param title must be str!")

        self.content_ += "##### {title}\n".format(title=title)
        return self

    def add_content(self, content: str, is_wrap=True) -> "Markdown":
        """
        添加正文内容
        :param content: str  正文内容
        :param is_wrap: bool 是否换行
        :return: Markdown 对象
        """
        if type(content) != str:
            raise TypeError("The param content must be str!")

        content_ = content + "\n" if is_wrap else content
        self.content_ += content_
        return self

    def add_list(self, content_dict: dict) -> "Markdown":
        """
        添加列表
        :param content_dict: dict 列表信息字典
        :return: Markdown 对象
        """
        if type(content_dict) != dict:
            raise TypeError("The param content_dict must be dict!")

        self.content_ += self._add_list_iter(content_dict, level=0) + "\n"
        return self

    def _add_list_iter(self, content_dict: dict, level: int = 0) -> str:
        list_str = ""
        style = content_dict['style'] if "style" in content_dict else "ul"

        if style == "ol":
            for index, content in enumerate(content_dict['content']):
                if type(content) == dict:
                    list_str += self._add_list_iter(content, level=level + 1)
                else:
                    list_str += "\n{indent}{style}. {content}".format_map({
                        "indent": "\t" * level,
                        "style": index + 1,
                        "content": content
                    })
        else:
            for index, content in enumerate(content_dict['content']):
                if type(content) == dict:
                    list_str += self._add_list_iter(content, level=level + 1)
                else:
                    list_str += "\n{indent}- {content}".format_map({
                        "indent": "\t" * level,
                        "style": index + 1,
                        "content": content
                    })
        return list_str

    def add_wrap(self) -> "Markdown":
        """
        添加换行符
        :return: Markdown 对象
        """
        self.content_ += "\n"
        return self

    def add_image(self, image_path: str, image_text: str = "无") -> "Markdown":
        """
        添加图片
        :param image_path: str 图片地址
        :param image_text: str 图片内容
        :return: Markdown 对象
        """
        if type(image_path) != str or type(image_text) != str:
            raise TypeError("The param content must be str!")

        self.content_ += "![{text}]({path})".format_map({
            "text": image_text,
            "path": image_path
        })
        return self

    def add_link(self, link_path: str, link_text: str = "链接内容") -> "Markdown":
        """
        添加网页链接
        :param link_path: str 链接地址
        :param link_text: str 链接内容
        :return: Markdown 对象
        """
        if type(link_path) != str or type(link_text) != str:
            raise TypeError("The param content must be str!")

        self.content_ += "[{text}]({path})".format_map({
            "text": link_text,
            "path": link_path
        })
        return self

    def add_code(self, code_content: str, code_type: str) -> "Markdown":
        """
        添加代码区域
        :param code_content: str 代码内容
        :param code_type:    str 代码类型
        :return: Markdown 对象
        """
        if type(code_content) != str or type(code_type) != str:
            raise TypeError("The param content must be str!")

        code_type = code_type if type(code_type) == str else ""
        code_content = code_content if type(code_content) == str else ""

        self.content_ += "```{type}\n{content}\n```\n".format_map({
            "type": code_type,
            "content": code_content
        })
        return self

    def add_table(self, table_info: dict, data: iter) -> "Markdown":
        """
        添加表格
        :param table_info: dict 表格信息字典
        :param data:       iter 表格数据
        :return: Markdown 对象
        """
        if type(table_info) != dict:
            raise TypeError("The param table_info must be dict!")

        table_str = ""
        cols = table_info.keys()
        indexs = [table_info[col].get('index', index) for index, col in enumerate(cols)]
        align_dict = {"left": ":---", "center": ":---:", "right": "---:"}

        # 设置表头信息
        table_str += " | ".join(cols) + "\n"
        table_str += " | ".join([align_dict[table_info[col]['align']]
                                 if table_info[col]['align'] in align_dict else ":---" for col in cols]) + "\n"

        # 设置表格内容
        for item in data:
            table_str += " | ".join([str(item[index]) for index in indexs]) + "\n"

        self.content_ += "\n" + table_str + "\n"
        return self

    def write(self, output_path: str, is_cover=False) -> None:
        """
        生成 markdown 文件
        :param output_path: str  导出路径
        :param is_cover:    bool 是否覆盖
        :return:
        """
        if type(output_path) != str:
            raise TypeError("The param output_path must be str!")

        file_mode = "w" if is_cover else "x"

        with open(output_path, mode=file_mode, encoding="utf-8") as file:
            file.write(self.content_)


if __name__ == '__main__':
    md = Markdown()
    md.add_h1("数据类型")\
        .add_content("Tensorflow 中的基本数据类型包含了数值型、字符串型和布尔型。")\
        .add_h2("数值类型")\
        .add_content("数值类型的张量是 TensorFlow 的主要数据载体，具体可划分为：")\
        .add_table({
            "名称": {"align": "left", "index": 0},
            "英文": {"align": "left", "index": 1},
            "维度": {"align": "left", "index": 2},
            "shape": {"align": "left", "index": 3},
            "描述": {"align": "left", "index": 4}
        }, [
            ["标量", "Scalar", 0, "[]", "单个的实数"],
            ["向量", "Vector", 1, "[n]", "n 个"]
        ])\
        .add_content("【轴（Axis）】：张量的每个维度也叫做轴，在机器学习中通常被特征向量，代表了具体的物理含义。例如，Shape 为 [2, 32, 32, 3] 的张量共有 4 维，如果表示图片数据的话，每个维度/轴代表的含义分别是——图片数量、图片高度、图片宽度、图片通道数，其中 2 代表了 2 张图片，32 代表了高宽均为 32，3 代表了 RGB 3 个通道。")\
        .add_wrap()\
        .add_content("【示例】：获取张量的信息。")\
        .add_code(">>> x = tf.constant([1, 2., 3.3])\n>>> x\n<tf.Tensor: id=1, shape=(3,), dtype=float32, numpy=array([1. , 2. , 3.3], dtype=float32)> ", "python")\
        .add_list(
            {"style": "ol", "content": ["id: TensorFlow", "shape", {"style": "ul", "content": ["haha", "test"]}, "numpy()"]}
        )\
        .write("test.md", is_cover=True)
