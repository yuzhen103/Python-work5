#!/usr/bin/env python
# coding: utf-8

# In[3]:


import speech_recognition
r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = r.listen(source)


# In[4]:


r.recognize_google(audio, language = 'zh-TW')


# In[5]:


import speech_recognition
r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = r.listen(source)


# In[6]:


r.recognize_google(audio, language = 'zh-en')


# In[7]:


import speech_recognition
r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = r.listen(source)


# In[8]:


result = r.recognize_google(audio, language = 'ja')


# In[9]:


print(result)


# In[ ]:




