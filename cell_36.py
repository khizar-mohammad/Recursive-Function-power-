#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def power(base,ex):
  if ex>0:
    return (base * power(base,ex-1))
  elif ex == 0:
    return 1
  else:
    print("error")

