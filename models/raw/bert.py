#!/usr/bin/env python
# coding: utf-8

# # Jupyter documentation for usage of Bert Base NER model for Person Recognition

# ## Imports
# 
# Also required for Bert to work is installing `torch` package.

# In[ ]:


from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification


# ## Initialization
# 
# Initializes token and model from pretrained dataset.

# In[ ]:


tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")


# ## Pipeline
# 
# Creates pipeline to use for comunicating with the model.

# In[3]:


nlp = pipeline("ner", model=model, tokenizer=tokenizer)


# ## Functions
# 
# Functions to use the model.

# In[4]:


def process_message(message: str) -> list[str]:
    """
    Runs given message through pretrained Bert NER model and returns people
    """
    result = nlp(message)
    names = [obj['word'] for obj in result if obj['entity'] == 'B-PER']
    return names


# In[5]:


def get_example_message() -> str:
    return "My name is Wolfgang and I live in Berlin"


# In[6]:


def process_example() -> list[str]:
    """
    Runs an example string through pretrained Bert NER model and returns people.
    """
    return process_message(get_example_message())


# ## Example
# 
# Runs model with example message and prints results.

# In[7]:


test = process_example()
print(test)

