#!/usr/bin/env python
# coding: utf-8

# In[5]:


from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification


# In[6]:


tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")


# In[9]:


nlp = pipeline("ner", model=model, tokenizer=tokenizer)


# In[11]:


def process_message(message: str) -> list[str]:
    """
    Runs given message through pretrained Bert NER model and returns people
    """
    result = nlp(message)
    names = [obj['word'] for obj in result if obj['entity'] == 'B-PER']
    return names


# In[ ]:


def get_example_message() -> str:
    return "My name is Wolfgang and I live in Berlin"


# In[12]:


def process_example() -> list[str]:
    """
    Runs an example string through pretrained Bert NER model and returns people.
    """
    return process_message(get_example_message())

