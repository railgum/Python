import creater_file as html
import xml_generator as xml
import data_provider as dp

# print(html.create())
# print(xml.create())

# print(html.new_create())
# print(xml.new_create())

xml.new_create(dp.data_collection())
html.new_create(dp.data_collection())
