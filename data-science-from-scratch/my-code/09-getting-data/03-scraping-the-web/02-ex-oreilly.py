# * Example: O'Reilly Books About data
#   - Examine how many data books O'Reilly has published over time
#   NOTE: Most of this doesn't work since the demo html is different now
import requests
import json
import matplotlib as plt
from collections import Counter
from bs4 import BeautifulSoup
from time import sleep
from dateutil.parser import parse

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
title = tds.find('div', 'thumbheader').a.text

# author is in the text of the dic with AuthorName
author_name = tds.find('div', 'AuthorName').text
authors = [x.strip() for x in re.sub("^By ", "", author_name).split(",")]

# ISBN seems to be contained in the link that's in the thumbheader <div>
isbn_link = tds.find("div", "thumbheader").a.get("href")

# re.match captures the part of the regex in parenthesis
isbn = re.match("/product/(.*)\.do", isbn_link).group(1)

# the dats is the contents of <span class="directorydate ">
date = tds.find("span", "directorydate").text.strip()


# Put this together into a function
def book_info(td):
    """given a BeautifulSoup <td> Tag representing a book.
    extract the book's details and return a dict"""

    title = td.find("div", "thumbheader").a.text
    by_author = td.find("div", "AuthorName").text
    authors = [x.strip() for x in re.sub("^By ", "", author_name).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).group(1)
    date = td.find("span", "directorydate").text.strip()

    return {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "date": date
    }


# Now, we're ready to scrape
base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
    "data.do?sortby=publicationDate&page="

books = []

NUM_PAGES = 31

for page_num in range(1, NUM_PAGES + 1):
    print("souping page", page_num, ",", len(books), " found so far")
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))

    sleep(30)


# %% Plot the number of books published each year
def get_year(book):
    """book["date"] looks like 'November 2014' so we need to
    split on the space and then take the second piece"""
    return int(book["date"].split()[1])


# 2014 is the last complete year of data (when this was made)
year_counts = Counter([get_year(book) for book in books
                      if get_year(book) <= 2014])

years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]

plt.plot(years, book_counts)
plt.ylabel("# of data books")
plt.title("Data is Big!")
plt.show()
