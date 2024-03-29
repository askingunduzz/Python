# -*- coding: utf-8 -*-
"""yedinciDers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oqzyVZdjsKAGtFj_r41egi8UpCZz1Y6U
"""

##this week we will talk about numpy library, on time permitting we will implement our own KNN classifier from scratch.
##Next week we will train a simple linear regressor from scratch as well on time permitting.
A=[1,2,3]
B=[1,2,3]

A+B

import numpy as np

##1D vectors, 2D matrices, 3D higher tensors/multidimensional matrices
##numpy arrays behave like vectors
##these libraries are writtn in C
A=[1,2,3,4,5,-2]

##lets concert this guy to a numpy array
A=np.array(A)

A

A.dtype  ##hocada int32 yazdı why

B=[1,4,5.4]
B=np.array(B)  ##convvertes everything to floats

B.dtype

B=[1,4,5.4]

B=np.array(B, dtype=np.int32)

B ##hocada sdce array([1,4,5]) yazıyor?

dir(B)

from numpy import random

random.randn()

np.random.randn()

from matplotlib import pyplot as plt

plt.hist(np.random.randn(10000),bins=100,density=True);

np.random.randn(2,2)     ##random array of 2*2

np.random.rand()    ##uniform distribution

plt.hist(np.random.rand(10000),density=True);      ##; koyup koymayınca değişiyor!

np.random.randint(0,5,size=100)

np.random.randint(0,5,size=10)

##one can do arithmetic with numpy arrays! its fastif you dont screw up

A=np.random.randn(100)
B=np.random.randn(100)

A+B     ##componentwise addition, vector addition

A*B

(A*B).shape
##A*B componentwise multiplication of two arrays of the same size

A=np.random.randn(100)
##B=np.random.randn(5)     ##this is not possible (A*B)    1 olcak ya da 100
B=np.random.randn(1)

A*B

A=np.array([1,2,3,4,5])
B=np.random.randn(1)

B ##array length 1 ya da A'nınkiyle aynı olcak

A*B

A*B == B*A

L=[1,2,-3,-4]      ##this is a list. numpy olmadan array olmaz
##you cant compare a list with a number: L>1

L=np.array([1,2,-3,-4])

L>1     ## broadcasting, this guy is comparing not the array with 1, but components of the array.

M=np.array([1,2,3,4])
M>L ##the components are compared  for loopla her şeyi karşıalştırıyo gibi düşüncebilirsin   ##array of booleans

M[0]

M[-1]

M[1:3]  ##FİRST AND SECOND.

M[M>L]  ##true olan degerleri basıyor

for i in range(10):
  print(i)

for i in range(0,10,2):  ##sdce int olabilir   for i=0, i<10 !!
  print(i)

for i in np.arange(0,10,0.2):  ##numpy!   ###rational stepsizes are allowed in numpy arange
  print(i)

##machine learning kısmına giricez biraz
##2nd hour will be very important lesson!!!!
##classifier, regressor - ale
L=[1,2,3,4,5]
L = np.random.randn(10,15,20)  ##this guy has three axes
(10,15,20) ##axis = 0(10), axis = 1(15), axis=2(20)

L=np.random.randn(100)

L

np.mean(np.random.randn(100),axis=0)

L.mean()

##np.mean()

L = np.random.randn(10,15,20)

L.mean(axis=0)

L.mean(axis=0).shape

L.mean(axis=1).shape  ##nice , mantığını çizerek de yap. 3 boyutlu diktörtgen sdce

L.std(axis=2)

L.std(axis=1)

L.std(axis=2), L.var(axis=2)

np.var(L,axis=2)

L+1    ##1 İS ADDED TO AL COMPONENTS OF l broadcasting

##transpose of this matrix 2*2 or 3*3 idk
L=np.random.randn(10,15)

L

L.T   ##SİMPLEST solution but doesnt work properly always

(L.T).shape

L.shape

L=np.random.randn(10,12,13,15)   ##axes =0,1,2,3
L.shape

np.transpose(L,[0,1,2,3]).shape ##you want to interchange axis 1 and 3

np.transpose(L,[3,2,1,0]).shape

np.transpose(L,[0,2,1,3]).shape

L=np.random.randn(100)
L

L.reshape(2,50)   #you reshape the array
L

L.reshape(2,5,10).shape

L=np.random.randn(10,12,13,15)

L.reshape(-1)

L.reshape(-1).shape     ##flattens the array

L=np.random.randn(3,4,4,3)

np.max(L)

np.max(L,axis=0).shape

np.min(L,axis=1).shape

np.argmax(L,axis=0) ##this is the place where the max is attained

np.argmax(L,axis=0).shape

np.argmin(L,axis=0).shape

##more concrete example
A=np.array([[1,6],[3,5]])

A.mean(0) ##hocada farklı outpu

A.max()

A.max(0)   ##dikey çizgideki maxları aldı

A.max(1)  ##yatay çizgideki max ları aldı

A.mean(0)

np.argmax(A,1)   ##maximum int in arrydaki yerini verdi

np.argmax(A,0)   ##maximum int in arrydaki yerini verdi

np.argmin(A,0)

A

np.unique([1,2,3,4,5,-1,4,5,6,1,23,3])

np.unique([1,2,3,4,5,-1,4,5,6,1,23,3],return_index=True)    ##aşağıda çıkan o elementlerin indexleri

np.unique([1,2,3,4,5,-1,4,5,6,1,23,3],return_index=True,return_counts=True)    ##bincounts: kaç kere olduğu

## k nearest neighbours algorithm
##n_neighbours=5 you look at the 5 nearst neighbours
##en çok hangi renkten varsa o classtan seçiliyo
## we are given X_train, y_train
##we are given sample
## measure all distances between X_train and sample  -x_train: matrix, sample: a single vector
##sample list = the distances , you sort them and get the arguments of sorted distances
##pick the classes of the first 5 ones., if in majortiy we have blue classes: answer is blue. knn  ##classsification ı hoca ypıcak regressionı biz yapıcaz

np.sort(np.random.randn(100))  ##its in ascending order

np.argsort(np.random.randn(100))

##third hour we will cry
##we will implemetn our own KNN algorithm from scratch

from sklearn.datasets import load_iris

X,y=load_iris(return_X_y=True)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =train_test_split(x,y)

class KNNClassifier:             ## __ ne için var
  def __init__(self,n_neighbours=5):
    self.n_neighbours=n_neighbours
  def fit(self,X_train,y_train):
    self.X_train=X_train
    self.y_train=y_train
  def predict(self,X_text):
    pass
  def __predictind__(self,x_sample):   ##this is our example  predictindividual
    distances=np.lialg.norm(self.X_train-x_sample,axis=1)
    sorted_distances=np.argsort(distances)
    nearest_n=sorted_distances[:self.n_neighbours]
    return nearest_n

X_train=np.random.randn(100,5)  ##100 rows 5 columns

sample=np.random.rand(1,5)

X_train - sample   ##does backtracing?      ##substrcact sample from each row of x_train

np.linalg.norm([1,1])  ##kök2

(X_train-sample).shape

np.linalg.norm(X_train-sample)    ##100e 5lik tüm elementlerin karesini alıp toplicak ve kareköke alcıak

np.linalg.norm(X_train-sample, axis=1)   ## 0 dikey 1 yatay saplıyor

class KNNClassifier:             ## __ ne için var
  def __init__(self,n_neighbours=5):
    self.n_neighbours=n_neighbours
  def fit(self,X_train,y_train):
    self.X_train=X_train
    self.y_train=y_train
  def predict(self,X_text):
    return np.array([self.__predictind__(x_sample) for x_sample in X_test])
  def __predictind__(self,x_sample):   ##this is our example  predictindividual
    distances=np.lialg.norm(self.X_train-x_sample,axis=1)
    sorted_distances=np.argsort(distances)
    nearest_n=sorted_distances[:self.n_neighbours]
    proposed_labels=y_train[nearest_n]
    x,y,z=np.unique(proposex_labels,return_index=True,return_counts=True)  ##1,1,2,2,2 vermişti onların kaç kere sayılığını buldu
    return proposed_labels[np.max(x)]    ##alede elle yazıcz bunu  ##ALEDE SADECE BURADA DEĞİŞİKLİK YAPICAKSINZ DEDİ
    return x,y,z,proposed_labels

knn=KNNClassifier()
knn.fit(X_train,y_train)
labels=knn.predict(X_test)   ##predict ve predictind
distances = knn.__predictind__(X_test[0]) ## x testin içine 0... bir sürü rakam koyup y testin içine koyuyz deneme amaçlı

distances  ##the argument of the nearet neighbours

y_test[0]  ##xtest 24 yapıp y test 24 de yap

np.mean(labels==y_test)  ##doğruluk yüzdesini vreiyo buduğun değerin

##alede çok bi şey değişmicek burda proposed label demicek de işte ihtiyacınız olan değerler olcak
##nearest y değerlini alıp average licaz prpopsed labels kısmında değişklik olcak