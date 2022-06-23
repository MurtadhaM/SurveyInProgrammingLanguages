# -*- coding: utf-8 -*-
# Author: Murtadha Marzouq
# Description: This file contains the functions to fetch the topics from the website.

import json
import requests
from bs4 import BeautifulSoup
import re


# Preparing the dictionary
urls_arr = {'Belk College of Business': 'https://pages.charlotte.edu/connections/group/college-of-business/'
            ,'College of Arts + Architecture':'https://pages.charlotte.edu/connections/group/college-of-arts-and-architecture//' 
            ,'College of Computing & Informatics':'https://pages.charlotte.edu/connections/group/cci' 
            ,'College of Education ':'https://pages.charlotte.edu/connections/group/coed/' 
            ,'College of Health & Human Services':'https://pages.charlotte.edu/connections/group/chhs/' 
            ,'College of Liberal Arts & Sciences':'https://pages.charlotte.edu/connections/group/clas/' 
            ,'Lee College of Engineering':'https://pages.charlotte.edu/connections/group/college-of-engineering/' 
            ,'School of Data Science (SDS)':'https://pages.charlotte.edu/connections/group/school-of-data-science-sds/'}
# departments = urls_arr.keys()
# urls = urls_arr.values()
topics_group = {}
    
def topic_fetch(department , url):
    '''
    Fetches the topics from the given url and stores it in a dictionary.
    :param department: The department for which the topics are to be fetched.
    :param url: The url from which the topics are to be fetched.
    :return: A dictionary containing the topics and their respective counts.
    '''
    try:
            # because of inconsistent html structure, we need to use beautiful soup to parse the html
            if department == 'College of Health & Human Services':
                soup  = BeautifulSoup(requests.get(url).text, 'html.parser').find('div',{'id':'d3-word-cloud-control-2'} ) 
            else:
                soup  = BeautifulSoup(requests.get(url).text, 'html.parser').find('div',{'id':'word-cloud-control-2'} )             
            values = soup.find('input', attrs={'class', 'tags'})['value'] 
            topics = re.findall('"name":"(.*?)",', values)
            counts = re.findall('"count":(.*?),"', values)
            urls = re.findall('"url":"(.*?)"}', values)
            # populating the dictionary
            for i in range(len(topics)):
                topics_group[department]["topics"][topics[i]] = {
                    'count': counts[i],
                    'url': urls[i].replace('\\/', '/')
                }
    except Exception as e:
            print(e.args)
    print(topics_group)        
    return topics_group       


def group_stats(url):
    try:
            soup  = BeautifulSoup(requests.get(url).text, 'html.parser').find('div',{'class':'found-posts'} )             
            value = soup.text
            print(value)
            return value
    except Exception as e:
            print(e.args) 

# debugging 
#urls_arr = {'College of Health & Human Services': 'https://pages.charlotte.edu/connections/group/chhs/'}

# fetching the topics for each department
for department, url in urls_arr.items():
    print(department, url)
    topics_group[department] = {}
    topics_group[department]["topics"] = {}
    topics_group[department]["number of employees"] = group_stats(url)
    topic_fetch(department, url)

# Writing the dictionary to a json file    
with open('logs/topics_group.json', 'w') as f:
        f.write(json.dumps(topics_group))    
print(json.dumps(topics_group, indent=4))


