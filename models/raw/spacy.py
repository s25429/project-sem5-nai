#!/usr/bin/env python
# coding: utf-8

# # Jupyter documentation for usage of Spacy NER model for Person Recognition

# ## Imports
# 
# Also required for Spacy to work is to run `python -m spacy download en_core_web_sm`.

# In[1]:


import spacy
from spacy.lang.en.examples import sentences


# ## Pipeline
# 
# Creates pipeline to use for comunicating with the model.

# In[2]:


nlp = spacy.load("en_core_web_sm")


# ## Functions
# 
# Functions to use the model.

# In[3]:


def process_message(message: str) -> list[str]:
    """
    Runs given message through pretrained Spacy model and returns PERSON label
    """
    names = []
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)
    return names


# In[4]:


def get_example_message() -> str:
    return "My name is Wolfgang and I live in Berlin"


# In[5]:


def process_example() -> list[str]:
    """
    Runs an example string through pretrained Spacy model and returns people.
    """
    return process_message(get_example_message())


# ## Example
# 
# Runs model with example message and prints results.

# In[6]:


test = process_example()
print(test)

