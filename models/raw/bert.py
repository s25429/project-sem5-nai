#!/usr/bin/env python
# coding: utf-8

# In[5]:


from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification


# In[6]:


tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")


# In[9]:


nlp = pipeline("ner", model=model, tokenizer=tokenizer)


# In[10]:


def get_example():
    result = nlp("My name is Wolfgang and I live in Berlin")
    names = [obj['word'] for obj in result if obj['entity'] == 'B-PER']
    return names

