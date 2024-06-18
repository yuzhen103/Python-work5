#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install gTTS')


# In[2]:


get_ipython().system(' pip install pygame')


# In[3]:


from gtts import gTTS
tts = gTTS(text = '早安，你好。', lang = 'zh-TW')
tts.save('good morning.mp3')


# In[4]:


from pygame import mixer
mixer.init()
mixer.music.load('good morning.mp3')
mixer.music.play()


# In[5]:


from gtts import gTTS
tts = gTTS(text = 'おはよう', lang = 'ja')
tts.save('good morning_ja.mp3')


# In[6]:


from pygame import mixer
mixer.init()
mixer.music.load('good morning_ja.mp3')
mixer.music.play()


# In[7]:


import tempfile
def speak(sentence):
    with tempfile.NamedTemporaryFile(delete = True) as fp:
        tts = gTTS(text = sentence, lang = 'zh-CN')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()


# In[8]:


speak('早安，又是美好的一天！')


# In[9]:


import tempfile
def speak(sentence):
    with tempfile.NamedTemporaryFile(delete = True) as fp:
        tts = gTTS(text = sentence, lang = 'ja')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()


# In[10]:


speak('これやこの 行くも帰るも 別れては 知るも知らぬもあふ坂の関')


# In[2]:


from pygame import mixer
mixer.init()
mixer.music.load("Chopin - Nocturne op.9 No.2.mp3")
mixer.music.play()


# In[ ]:




