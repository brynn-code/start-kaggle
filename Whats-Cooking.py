# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
import json
from sklean import tree

class recipe:
    def __init__(self, id, cuisine, ingredients):
      self.id = id
      self.cuisine = cuisine
      self.ingredients = ingredients

    def __str__(self):
        """
            implements toString method
        """
        return 'this recipe\'s id : {} , cuisine : {}, ingredients : {}'.format(self.id, self.cuisine, self.ingredients)  
    
data = []
classes = set()
foods = set()

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        if 'train' in filename:
            with open(dirname + "/" + filename, "r") as f:
                data_dic = json.loads(f.read())
                for dic in data_dic:
                    data.append(recipe(id = dic['id'], cuisine = dic['cuisine'], ingredients = dic['ingredients']))
                    classes.add(dic['cuisine'])
                    for food in dic['ingredients']:
                        foods.add(food)
 
# 获取所有类别,再转成列表,使得可以用下标访问 
classes = list(classes)
foods = list(foods)
                    
print(len(data))
print(data[0].cuisine)
print(len(classes))
print(len(foods))

# 0.尝试一下决策树

clf = tree.DecisionTreeClassifier()

# 1.确定分类器(分类函数)
# 2.确定损失函数
# 3.训练(有点好奇, 还需要划分validation set吗)
# 4.评估



# Any results you write to the current directory are saved as output.