from lxml import etree

# 创建一个XML解析器
parser = etree.XMLParser()
# 解析XML文件
tree = etree.parse('example.xml', parser)

# 选择所有具有'id'属性的元素
elements_with_id = tree.xpath('//*[@id]')

# 选择所有标签名为'tagname'的元素
tagname_elements = tree.xpath('//tagname')

# 选择所有属性'name'值为'value'的元素
elements_with_specific_attribute = tree.xpath("//*[@name='value']")

# 选择所有文本内容为'text_value'的元素
text_elements = tree.xpath("//*[text()='text_value']")

# 组合多个过滤条件
combined_elements = tree.xpath("//tagname[@attribute='value' and text()='text_value']")

# 通过索引过滤，选择第一个'tagname'元素
first_element = tree.xpath("//tagname[1]")
