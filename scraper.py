from bs4 import BeautifulSoup
import requests
from Powerball import Powerball

## Get the site html
def get_site_html(url):
  response = requests.get(url)
  return response


## Get the specified css elemnt from the html
def get_html_element(html, element):
  soup = BeautifulSoup(html.text, "html.parser")
  return soup.findAll(element)


## Extract all relavent data from the table rows that we scraped
def scrape_powerball_numbers(html):

  soup = BeautifulSoup(html.text, "html.parser")
  tr = soup.findAll('tr')

  result = []

  for i in range(1, len(tr) - 1):

    td = tr[i].findAll('td')
    date = td[0].text
    
    # All data before and during 2015 is irrelavent
    if "2015" in date:
      return result

    numbers = [int(td[i].text) for i in range(1,6)]
    numbers.sort()
    powerball = int(td[6].text)

    result.append(
      Powerball(date, numbers, powerball)
    )

  return result
