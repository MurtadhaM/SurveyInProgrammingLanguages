# -*- coding: utf-8 -*-
# Author: Murtadha Marzouq
# Description: This is the main crawler file.
import json
from bs4 import BeautifulSoup
import pandas as pd


# TODO
# support sessions by checking for stored staff info and if they don't exist then get them from the website --Completed
# For each web request, save the outputed HTML file for future use and mining and to also reduce network traffic --Completed
# Tor connection option for the program to anonymize the traffic and avoid detection -- Completed
# setting up the session (visited urls )  -- Completed


# Setting up variables to be used in the program
urls = []
people = []
UNCC = {'Belk College of Business': {}, 'College of Arts + Architecture': {}, 'College of Computing & Informatics': {}, 'College of Education': {}, 'College of Health & Human Services': {}, 'College of Liberal Arts & Sciences': {}, 'Lee College of Engineering': {}}
UNCC['Belk College of Business'] = {'Business Info Systems/Operations': {}, 'Economics': {}, 'Finance': {}, 'Management': {}, 'Marketing': {}, 'Turner School of Accountancy':{}}
UNCC['College of Arts + Architecture'] = {'Art & Art History': {}, 'Dance': {}, 'Music': {}, 'Performing Arts Services': {}, 'School of Architecture': {}, 'Theatre':{}}
UNCC['College of Computing & Informatics'] = {'Bioinformatics and Genomics' : {}, 'Bioinformatics Research Center': {}, 'Computer Science': {}, 'Software & Information Systems':{}, 'School of Data Science (SDS)': {}}
UNCC['College of Education'] = {'Counseling': {}, 'Ctr For STEM Education': {}, 'Educational Leadership': {}, 'Middle Grades Secondary & K-12': {}, 'Reading & Elementary ED': {}, 'School & Community Partnerships': {}, 'Special Ed & Child Dev':{}}
UNCC['College of Health & Human Services'] = {'Kinesiology': {}, 'Public Health Sciences': {}, 'School of Nursing': {}, 'School of Social Work':{}}
UNCC['College of Liberal Arts & Sciences'] = {'Africana Studies': {}, 'Anthropology': {}, 'Biological Sciences': {}, 'Chemistry': {}, 'Communication Studies': {}, 'Criminal Justice and Criminology': {}, 'English': {}, 'Geography and Earth Sciences': {}, 'Global Studies': {}, 'History': {}, 'Languages and Culture Studies': {}, 'Mathematics and Statistics': {}, 'Philosophy': {}, 'Physics and Optical Science': {}, 'Political Science and Public Administration': {}, 'Psychological Science': {}, 'Religious Studies': {}, 'Sociology': {}, 'Writing, Rhetoric, and Digital Studies':{}}
UNCC['Lee College of Engineering'] = {'Civil and Environmental Engr': {}, 'Electrical & Computer Engineering': {}, 'Engineering Tech & Constr Mgmt': {}, 'EPIC': {}, 'Mech Engineering & Engineering Sci': {}, 'Student Dev & Success': {}, 'Systems Engin & Engin Management':{}}

# a master array to store all the staff members
All_STAFF_INFOMATION = []
TOR_FLAG = False


# first start tor service on port 9050 by running the command:
# tor SocksPort 9050
def get_tor_session():
    '''
    Creates a tor session and returns it.
    :return: A tor session.
    '''
    import requests
    if TOR_FLAG:
        
        print('enabling tor')
        # check if tor is running
        try:
            
            session = requests.session()
            
            # Tor uses the 9050 port as the default socks port
            session.proxies = {'http':  'socks5://127.0.0.1:9050',
                            'https': 'socks5://127.0.0.1:9050'}
            
            current_ip = session.request('GET', 'http://httpbin.org/ip').text
            print('tor session established with IP ' + current_ip.split('origin')[1])
            
            return session 
        except Exception as e:
            print(e)
            print('Error getting tor session')
            print('Please make sure tor is running or disable the TOR_FLAG')
            print('Exiting program')
            exit()   
        return session
    else:
        print('tor not enabled')
        return requests

requests = get_tor_session()


class Person :
    def __init__(self, link):
        '''
        Initializes the class with the required parameters.
        :param link: The link of the website to be scraped.
        '''
        self.name = " "
        self.academic_interests = ""
        self.department = " "
        self.bio = " "
        self.link = link
        self.college = " "
        # fetching the information from the website
        self.get_info()

        
    
    def __str__(self):
        '''
        This function is used to convert the class object into a string.
        :return: A string of the object.
        '''
        try:
            return json.dumps(self.__dict__)
        except Exception as e:
            print(e)
    
    def get_college(self,department):
        '''
        This function returns the college name for a given department.
        :param department: The department for which the college is needed.
        :return: The college name.
        '''
        try:
            if department in UNCC.keys():
                return department
            for key in UNCC.keys():
                for subkey in UNCC[key].keys():
                    if department == subkey:
                        return key
            return " "
        except Exception as e:
            print(e)
    # fetching the information from the website and storing it in the class        
    def get_info(self):
        '''
        Collects the information about the staff.
        :return: None
        '''
        url = self.link
        # making a request to the website
        response = requests.get(url)
        # saving the log file
        soup = BeautifulSoup(response.text , 'html.parser')
        department = soup.find('div', class_='connection-groups').text.strip().split('\n')[0]
        academic_interests = soup.find('div', class_='connection-links columns-2')
        name = soup.find('div', class_='page-title').text.strip()
        bio = soup.find('div', class_='post-contents').text
        link = url
        # assigning the values to the class variables
        self.name = name
        self.department = department
        self.academic_interests = academic_interests.text.split('\n')
        self.college = self.get_college(department)
        self.link = link
        # CASTING THE BIO TO STRING
        self.bio = bio.replace('\n', ' ').replace('\u00a0', '').replace('\u201c', '')
        


def setup_initial_links():
    '''
    This function is used to setup the initial links for the people in the website.
    :return: A dataframe of the links.
    '''
    print('Setting up initial links')
    # getting the initial links from the website
    url = 'https://pages.charlotte.edu/connections/'
    # fetching the html file
    response = requests.get(url)
    soup = BeautifulSoup(response.text , 'lxml')
    script = soup.html.find_all('script')
    html_links = ''
    print('parsing elements to extract links')
    for elem in script:
        if elem.text.find('collapsing categories item') != -1:
            for line in elem.text.split('\n'):
                if line.find('href') != -1:
                    html_links += line.split(' = ')[1].replace('\\\'', '\"' ).replace(';', '').replace('\'', '')                
    s = BeautifulSoup(html_links, 'html.parser')
    links = {
        
   
     }
    
    anchor = s.find_all('a')
    for  tag in anchor:
        if 'people' in tag.get('href'):
            links[tag.text] = tag.get('href')

    print('converting to json the json file\n')
    array = [ {'name' : i, 'link' : links[i]} for i in links]
    print('links imported successfully')
    print('\n')

    # saving the files
    pd.DataFrame(data=links.values(), index=None, columns=['links']).to_csv('logs/links.csv', index=False)
    return pd.DataFrame(data=links.values(), index=None, columns=['links'])


# URL STORAGE  
urls = setup_initial_links()['links'].dropna().tolist()


# to map the department to the college
def get_college(department):
    '''
    This function takes in a department and returns the college to which it belongs.
    :param department: The department for which the college is needed.
    :return: The college to which the department belongs.
    '''
    try:
            if department in UNCC.keys():
                return department
            for key in UNCC.keys():
                for subkey in UNCC[key].keys():
                    if department in subkey:
                        return key
                
            return " "
    except Exception as e:
            print(e)       

def visited_update(url): 
    '''
    Removes the url from the list of visited urls.
    :param url: The url to be removed from the list of visited urls.
    :return: The updated list of visited urls.
    '''
    # remove the url from the file
    for link in  pd.read_csv('logs/links_data_filtered.csv')['links'].dropna().tolist():
        if link == url:
            # print(link)
            urls.pop(urls.index(link))
    return urls
    
def get_json():
    return json.dumps([UNCC])  # json.dumps([person.__dict__ for person in people])

# iterates through the urls and gets the information from the website
def get_all_links(links , limit):
    '''
    This function takes in a list of links and a limit on the number of links to be visited.
    It then calls the functions to visit the links and collect the data.
    :param links: A list of links to be visited.
    :param limit: The number of links to be visited.
    :return: None
    '''
           #for debugging
    #links = ['https://pages.charlotte.edu/connections/people/cwaites/', 'https://pages.charlotte.edu/connections/people/ewahler1/','https://pages.charlotte.edu/connections/people/jean-claude-thill/', 'https://pages.charlotte.edu/connections/people/bmuller7/' ,'https://pages.charlotte.edu/connections/people/astefan1/']
    try:
        for i in range(limit):
            visited_update(links[i])
            # addiing another person object to the People list
            person_added = Person(links[i]) 
            people.append(person_added)   
            print('added ' + person_added.name + ' to the datastore')   
            # logging the data to a file
            log_data()
    except Exception as e:
        print(e.args)
    # removing the entries that are already added    
    pd.DataFrame(urls , columns=['links'], index=None).to_csv('logs/links_data_filtered.csv', index=None)
    
# reads the data to a json file    
def read_UNCC():
    # Reads the data to a json file
    json_file = open('staff_data.json', 'r').readline(
)
    return json.loads(json_file)
# logging the data to a file        
def log_data():    
    '''
    Logs the data in a json file.
    :return: None
    '''
    with open('logs/log.json', 'w') as f:
        add_to_UNCC()
        f.write(json.dumps([UNCC]))
# save the data to a json file    
def save_UNCC():
    '''
    Saves the UNCC data to a json file.
    :return: None
    '''
    # Save the data to a json file
    with open('staff_data.json', 'w') as f:
        f.write(json.dumps([UNCC]))
        
# Adds the data to the master json file


def add_to_UNCC():
    '''
    Iterates through the UNCC saved dict and updates the information.
    :return: None
    '''
    try:
        for p in people:
            if len(p.college) > 2 and len(p.department) > 2 and p.department  != p.college and p.college != " ":
                #print('the person is : ' + p.name + ' and the department is : ' + p.department + ' and the college is : ' + p.college)
                UNCC[p.college][p.department][p.name] = ({ 'link' : p.link, 'bio' : p.bio, 'academic_interests': p.academic_interests  , 'college' : p.college, 'department' : p.department})
            elif  p.college  in UNCC.keys() :
                UNCC[p.college][p.name] = ({ 'link' : p.link, 'bio' : p.bio, 'academic_interests': p.academic_interests  , 'college' : p.college, 'department' : p.department})
        return json.dumps([UNCC])        
    except Exception as e:
        print(e.with_traceback) 
        print('error adding to UNCC')
        exit()

staff_links = pd.read_csv('logs/links.csv').drop_duplicates()['links'].dropna().tolist()
# start the scraping (Start insted of the main)
def start():
    # Starting the application
    # get staff information
    get_all_links(staff_links, len(staff_links))
    # update file
    add_to_UNCC()
    # save file
    save_UNCC()
# startin the application    
start()
# save_UNCC()
#print([UNCC])