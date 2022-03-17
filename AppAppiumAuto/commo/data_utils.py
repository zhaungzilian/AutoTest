import os

import yaml

# 读取yaml数据
def readYamldata(path):
    with open(path, "r+", encoding="utf-8") as file:
        pathdata = yaml.load(stream=file, Loader=yaml.FullLoader)
        return pathdata


def getdata():
    # 定位带父级目录
    rootpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # 关联父级目录，获取下面的目标文件
    path = os.path.join(rootpath, "config\desired_caps.yaml")

    return readYamldata(path)



if __name__ == '__main__':
    print(getdata())






















