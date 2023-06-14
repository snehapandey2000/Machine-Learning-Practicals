#!/usr/bin/env python
# coding: utf-8

# In[264]:


filename = 'thin.csv'


# In[265]:


def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# In[266]:


from csv import reader


# In[267]:


dataset = load_csv(filename)


# In[268]:


def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


# In[269]:


str_column_to_int(dataset, len(dataset[0]) - 1)


# In[270]:


print(dataset)


# In[293]:


# dataset len is no. of columns. And last wala cloumn class isliye -1
featureLen = len(dataset[0])-1


# In[271]:


import pandas as pd


# In[272]:


df = pd.DataFrame(dataset)


# In[273]:


classcol = df.iloc[:,-1:]


# In[274]:


# print(classcol)


# In[275]:


# print(df)


# In[276]:


classification = classcol.value_counts()


# In[277]:


# print(classification)


# In[278]:


totalclasses = len(classcol)


# In[279]:


# print(totalclasses)


# In[280]:


# print(len(dataset))


# In[281]:


Dict={}


# In[282]:


# for i in classcol:
#     print(i)


# In[283]:

# finding frequency
for i in range(len(classcol)):
    Dict[classcol.loc[i,len(dataset[0])-1]] = Dict.get(classcol.loc[i,len(dataset[0])-1], 0) + 1


# In[284]:


# print(Dict)


# In[285]:


# for key, val in Dict.items():
#     print(key, ":", val)


# In[286]:

# finding probability of each class
for key, val in Dict.items():
    Dict[key] = (Dict[key]/totalclasses)


# In[287]:


# for key, val in Dict.items():
#     print(key, ":", val)


# In[318]:


featureDict = {}
# isme feature no. : {class: list of iss iss feature me iss class pe feature values}

# In[319]:


# print(featureDict)


# In[320]:

# 
for i in range(len(dataset)):
    for j in range(featureLen):
        if j+1 not in featureDict:
            featureDict[j+1] = {}
        if dataset[i][-1] not in featureDict[j+1]:
                featureDict[j+1][dataset[i][-1]] = list()
        featureDict[j+1][dataset[i][-1]].append(dataset[i][j])
        # print(dataset[i][j])


# In[321]:


# print(featureDict)


# In[322]:


print("Enter test data vector")


# In[323]:


# print(featureLen)


# In[324]:


test = []
for i in range(featureLen):
    val = input("Enter" + str(i+1) + "feature: ")
    test.append(val)


# In[325]:


print(test)


# In[326]:


decisionClass = ' '
maxProb = 0


# In[331]:

# probability calculate, decision lere hain
for className, classProb in Dict.items():
    netProb = classProb
    # print(netProb)
    for j in range(featureLen):
        currFeatureList = featureDict[j+1][className]
        count = 0
        for featureValue in currFeatureList:
            if test[j] == featureValue:
                count+=1
        featureProb = count/len(currFeatureList)
        netProb*=featureProb
    if netProb > maxProb:
        maxProb = netProb
        decisionClass = className
    # print(className)
    # print(netProb)


# In[328]:


print(decisionClass)


# In[329]:


# print(maxProb)


# In[ ]:


# iris wale ka input
""" 
5.7
2.9
4.2
1.3
 """