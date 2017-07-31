# * Example: O'Reilly Books About data
#   - Examine how many data books O'Reilly has published over time
from bs4 import BeautifulSoup
import requests

url = "http://shop.oreilly.com/category/browse-subjects/" + \
      "data.do?sortby=publicationDate&page=1"

soup = BeautifulSoup(requests.get(url).text, 'html5lib')

# find all td thumbtext tag elements
tds = soup('td', 'thumbtext')
print(len(tds))


# Filter out videos
def is_video(td):
    """it's a video if it has exactly one pricelabel, and if the
    stripped text inside that pricelabel starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')

    return (len(pricelabels) == 1 and
            pricelabels[0].text.strip().startsWith('Video'))


print(len([td for td in tds if not is_video(td)]))

# the book title is the text inside <a> inside <div class="thumbheader">
title = td.find('div', 'thumbheader').a.text
