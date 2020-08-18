#!/usr/bin/env python
# coding: utf-8

# In[5]:


num=n=int(input())
list1=[]
count=0
x=True
while x:
    count+=1
    m=n%10
    list1.append(m)
    n=n//10
    if n==0:
        x=False
list2=[]
for i in range(count):
    s=(list1[i]**count)
    list2.append(s)

if sum(list2)==num:
    print("True")
else:
    print("False")
    

# another method
n=int(input())
digits=list(map(int,str(n)))
l=len(digits)
num=sum(list(map(lambda x:x**l,digits)))
if num==n:
    print("True")
else:
    print("False")


# In[ ]:




