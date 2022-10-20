#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Get num1 & num2 from user and return the
# greater one.
def signCompare(a, b):
    c = a - b
    if c >= 0:
        return a
    else:
        return b

num1, num2 =map(int, input().split())
signCompare(num1, num2)

