#!/usr/bin/env python
# coding: utf-8

# # Jupyter documentation for usage of OpenAI's ChatGPT for NER, specifically Person Recognition

# ## Imports
# 
# Package `dotenv` is installed by `pip install python-dotenv`.

# In[1]:


import os
from dotenv import load_dotenv
from openai import OpenAI


# ## Environment variables
# 
# For any work with OpenAI's API, an API key is required obtainable at [this link](https://platform.openai.com/api-keys).

# In[2]:


load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')


# ## Setup
# 
# API client is created and system message that specifies what actions we want ChatGPT to perform.

# In[3]:


client = OpenAI(api_key=OPENAI_KEY)
system_message = "You are an AI Named Entity Recognition helper and your task is to extract names and surnames of people in a text, given by the user. You reply only with a list of people's names that you extracted, separated by a coma. Example: if a user sends 'My name is Wolfgang and I live in Berlin with Anna.', you respond with 'Wolfgang, Anna'. If the name appears again, do not skip it."


# ## Functions
# 
# Functions to use the model.

# In[4]:


def process_message(message: str) -> list[str]:
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": message
            }
        ],
        stream=True,
    )
    names = ""

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            names = names + chunk.choices[0].delta.content
    
    return names.split(", ")


# In[5]:


def get_example_message() -> str:
    return "My name is Wolfgang and I live in Berlin"


# In[6]:


def process_example() -> list[str]:
    return process_message(get_example_message())


# ## Example
# 
# Runs model with example message and prints results.

# In[7]:


# test = process_example()
# print(test)

