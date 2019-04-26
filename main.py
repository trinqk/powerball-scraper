# LIBRARIES
import scraper
import math
import matplotlib.pyplot as plt
import numpy as np

### Note: This can probably be done more efficiently, I put this together as fast as I could

# Website URL
url = "https://www.wilottery.com/lottogames/powerballhistoryOD.aspx"

# Get HTML and extract numbers
html = scraper.get_site_html(url)
sorted_numbers = scraper.scrape_powerball_numbers(html)


# Numbers
# With the sorted_numbers, find how many times each number is picked, and "zones"
x1 = []
labels1 = ['0s', '10s', '20s', '30s', '40s', '50s', '60s']
sizes1 = [0, 0, 0, 0, 0, 0, 0]
for i in range(1, 70):
  x1.append(i)

numbers = [0] * 69
for number in sorted_numbers:
  for i in number.numbers:
    numbers[i-1] = numbers[i-1] + 1
    s1 = math.trunc(i/10)
    sizes1[s1] = sizes1[s1] + 1

f1, (ax1, ax2) = plt.subplots(1, 2)
ax1.bar(x1,numbers)
ax1.set_title('Number Occurences')
ax2.pie(sizes1, labels=labels1, autopct='%d')
ax2.set_title('Number Zones')


#Powerballs
# With the sorted_numbers, find how many times each powerball is picked, and "zones"
x2 = []
labels2 = ['0s', '10s', '20s']
sizes2 = [0, 0, 0]
for i in range(1, 27):
  x2.append(i)

powerball = [0] * 26
for number in sorted_numbers:
  pb = number.powerball
  powerball[pb-1] = powerball[pb-1] + 1
  s2 = math.trunc(pb/10)
  sizes2[s2] = sizes1[s2] + 1
  
f2, (ax1, ax2) = plt.subplots(1, 2)
ax1.bar(x2,powerball)
ax1.set_title('Powerball Occurences')
ax2.pie(sizes2, labels=labels2, autopct='%d')
ax2.set_title('Powerball Zones')

plt.show()