import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random,math
import os
random.seed(1234)

df=pd.read_csv('data.txt',sep=" ",dtype='Float64')
df_arr=df.values


xtrain=df_arr[:,0]
ytrain=df_arr[:,1]

flagc1=0
flagc2=0

for i in range(0,len(xtrain)):
        if flagc1==0:
            plt.scatter(xtrain[i],ytrain[i],s=20,c='r',marker='o',label='class1 train.txt')
            flagc1=1
        else:
            flagc1=0
            plt.scatter(xtrain[i], ytrain[i], s=20, c='r', marker='o')

plt.show()
k = 2
x1 =1#random.randint(0, 2998)
x2 =2#random.randint(0, 2998)
if (x1 == x2):
    x2 = x1 + 1
centroid1x = xtrain[x1]
centroid1y = ytrain[x1]
centroid2x = xtrain[x2]
centroid2y = ytrain[x2]

cluster1x=[]
cluster1y=[]
cluster2x=[]
cluster2y=[]
for kk in range(0,len(xtrain)):
        dist1=math.sqrt((xtrain[kk]-centroid1x)**2+(ytrain[kk]-centroid1y)**2)
        dist2=math.sqrt((xtrain[kk]-centroid2x)**2+(ytrain[kk]-centroid2y)**2)
        if(dist1<dist2):
            #plt.scatter(xtrain[kk], ytrain[kk], s=20, c='b', marker='x')
            cluster1x.append(xtrain[kk])
            cluster1y.append(ytrain[kk])
        else:
            #plt.scatter(xtrain[kk], ytrain[kk], s=20, c='g', marker='o')
            cluster2x.append(xtrain[kk])
            cluster2y.append(ytrain[kk])
prevcentroid1x=centroid1x
prevcentroid1y=centroid1y
prevcentroid2x=centroid2x
prevcentroid2y=centroid2y
calculate =0
for new in range(0,10):
    centroid1x = np.mean(cluster1x)
    centroid1y = np.mean(cluster1y)
    centroid2x = np.mean(cluster2x)
    centroid2y = np.mean(cluster2y)
    if(centroid1x!=prevcentroid1x or centroid1y!=prevcentroid1y or centroid2x!=prevcentroid2x or centroid2y!=prevcentroid2y):
        cluster1x=[]
        cluster2x=[]
        cluster2y=[]
        cluster1y=[]
        for kk in range(0,len(xtrain)):
            dist1 = math.sqrt((xtrain[kk] - centroid1x) ** 2 + (ytrain[kk] - centroid1y) ** 2)
            dist2 = math.sqrt((xtrain[kk] - centroid2x) ** 2 + (ytrain[kk] - centroid2y) ** 2)
            if (dist1 < dist2):
                cluster1x.append(xtrain[kk])
                cluster1y.append(ytrain[kk])
            else:
                cluster2x.append(xtrain[kk])
                cluster2y.append(ytrain[kk])
    else:
        calculate=new
        break
    prevcentroid1x=centroid1x
    prevcentroid1y=centroid1y
    prevcentroid2x=centroid2x
    prevcentroid2y=centroid2y
print(calculate)
plt.scatter(cluster1x, cluster1y, s=20, c='b', marker='x',label='Cluster 1')
plt.scatter(cluster2x, cluster2y, s=20, c='g', marker='o',label='Cluster 2')
plt.legend(loc='best')
plt.show()