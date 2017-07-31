# * HTML and the Parsing Thereof
#   - Use the *beautiful soup* library, which builds a tree out of
#   various elements on a web page, whilst providing a simple interface
#   to access the data
#   - Use *requests*, which is built for making HTTP requests
#   - Use *html5lib* which is useful for parsing HTML
from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

# We will typically work with tag objects, corresponding to the tags in the
# structure of HTML pages
first_paragraph = soup.find('p')

# Get the contents of a Tag using the *text* property
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

# Extract tag attributes by treating it like a dict
first_paragraph_id = soup.p.get('class')

# Get multiple tags at once
all_paragraphs = soup.find_all('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

# Find tags with a specific class
important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]

# Every <span> contained in a <div>
# will return same span if sits in multiple divs
spans_inside_divs = [span
                     for div in soup('div')
                     for span in div('span')]
