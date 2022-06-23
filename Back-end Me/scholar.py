#Author: Murtadha Marzouq
#Description: This script will scrape the Charlotte University staff and their publications
from scholarly import scholarly
import json
import requests
from bs4 import BeautifulSoup

'''
@description: This function will scrape the staff names from the staff page
@param: None
@return: Names of the staff
'''
def get_staff():
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
    names = links
    return names
# storing the staff names in variable
staff_names = get_staff()

'''
@description: fetching the author's publications from Google Scholar
@param: author's name
@return: author's publications
'''
def get_citations(author):
    try:
        # attempt to get the author's publications
        search_query = scholarly.search_author(author)
        # populate the author's publications
        author = next(search_query)

        # get the author's publications
        author_info = scholarly.fill( author, sections=['basics', 'counts','url_picture','name', 'citedby'])
        # Feed the author's publications to the json encoder
        name = author_info['name']
        counts = author_info['citedby']
        picture = author_info['url_picture']
        url = 'https://scholar.google.com/citations?user=' + author['scholar_id']
        author_info['url'] =  url
        # return the author's publications
        print(name + ' was found and has ' + str(counts) + ' publications')
        return json.dumps(author_info)
    except:
        print('author not found')
        pass
'''
@description: fetching the author's publications
@param: None
@return: None

'''
def main():
    for name in staff_names:
        data = get_citations(name)
    if data != None:
        # write the author's publications to a json file
        with open('staff_citations.json', 'a') as f:
            f.write(data)
            f.write('\n')


main()