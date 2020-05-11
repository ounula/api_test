import re
from common.myconfig import conf


# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# data = '{"member_id": #member_id#,"amount":600}'
# ----未使用正则之前的参数替换方法-------
# if "#phone#" in data:
#     data = data.replace("#phone#",conf.get_str("test_data","user"))
#
# if "#pwd#" in data:
#     data = data.replace("#pwd#",conf.get_str("test_data","pwd"))
# print(data)

# ------------使用正则进行替换----方式不通用----------
# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# r = "#.+?#"

# res2 = re.search(r, data)
# print(res2)
# data = data.replace(res2.group(), conf.get_str("test_data", "user"))
# print(data)

# res3 = re.search(r, data)
# print(res3)
# data = data.replace(res3.group(), conf.get_str("test_data", "pwd"))
# print(data)

# res1 = re.findall(r,data)
# print(res1)


# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'


# r = "#(.+?)#"
#
# res = re.search(r,data)
# # 判断匹配的结果是否为None
# if res:
#     item = res.group()
#     key = res.group(1)
#     print(item)
#     print(key)
#     data = data.replace(item,conf.get_str("test_data",key))
#
# res1 = re.search(r,data)
# if res1:
#     item = res1.group()
#     key = res1.group(1)
#     print(item)
#     print(key)
#     data = data.replace(item,conf.get_str("test_data",key))
#
# print(data)

class TestData:
    """这个类的作用：专门用来保存一些要替换的数据"""
    member_id = ""



def replace_data(data):
    r = r"#(.+?)#"
    # 判断是否有需要替换的数据
    while re.search(r, data):
        # 匹配出第一个要替换的数据
        res = re.search(r, data)
        # 提取待替换的内容
        item = res.group()
        # 获取替换内容中的数据项
        key = res.group(1)
        try:
            # 根据替换内容中的数据项去配置文件中找到对应的内容，进行替换
            data = data.replace(item, conf.get_str("test_data", key))
        except:
            data = data.replace(item, getattr(TestData,key))
    # 返回替换好的数据
    return data


# data = '{"mobile_phone":"#phone#","pwd":"#pwd#","user":#user#}'

# data1 = replace_data(data)
# data2 = replace_data(data1)
# print(data2)
# print(data1)

data2 = '{"member_id": #member_id#,"amount":600}'

data2 = replace_data(data2)
print(data2)

