#coding=utf-8

import collections
import os
import  csv
import glob



for dirpath, dirnames, filenames in os.walk(r'/home/xuan/amazon_csv/qa/panty/'):

    for filename in filenames:
        path = dirpath + "/" + filename
        #print('path')
        print(path)

        with open(path) as f:
            reader = [each for each in csv.DictReader(f)]
            #print(reader)
            line = []
            for row in reader:
                line.append(row['question'])
		line.append(row['answer'])

                # line.append(row['question'])
                # line.append(row['answer'])

        c = collections.Counter(str(line).replace('!',"").replace('.',"").replace(',',"").replace('?',"").replace('\'',"").replace('\"',"").replace('[',"").replace(']',"").replace('\n',"").replace('',"").split(" "))

        print("各单词出现的次数：\n")

        result=sorted(c.items(),key=lambda k:k[1],reverse=True)

        with open(path,'a') as f:
            for mess in result:
                f.write(str(mess).replace(",",":") + '\n')
