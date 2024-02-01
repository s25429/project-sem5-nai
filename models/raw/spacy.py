#!/usr/bin/env python
# coding: utf-8

# In[2]:


import spacy
from spacy.lang.en.examples import sentences


# In[3]:


nlp = spacy.load("en_core_web_sm")


# In[4]:


def process_message(message: str) -> list[str]:
    """
    Runs given message through pretrained Spacy model and returns PERSON label
    """
    names=[]
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)
    return names

