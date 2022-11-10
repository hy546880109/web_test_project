import os
import yaml
path = os.getcwd()
path = os.path.dirname(path)+'/test_data/data.yaml'

def read(path):
    with open(path,'r',encoding='utf-8')as f:
        data = f.read()
        result = yaml.load(data,Loader=yaml.FullLoader)
        return result


if __name__ == '__main__':
    # path = os.getcwd()
    # path = os.path.dirname(path)+'/test_data/data.yaml'
    print(read(path)['login']['url'])
