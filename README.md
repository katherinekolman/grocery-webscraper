# Pick n' Save Webscraper
This is a small webscraper I built a while ago that logs into my Pick n' Save account, grabs the grocery data from there, and then writes it to a CSV file. I was a bit curious about how much I was spending on food (really I wanted to know if I was buying too many Poptarts) so I made this using Python and Selenium using a webdriver for Firefox. It still needs a little more work, but most of it is there and functional.

Building this webscraper was a bit of a challenge at first. I had originally planned on using BeautifulSoup along with requests to scrape for data, but then I discovered the login page was rendered in JavaScript. I opted to use Selenium instead, which made things a lot easier, if a little slower.

## Resources
* Python 3+ (I think 2 would work as well, but I never tested it with that)
* [Selenium](https://www.seleniumhq.org/)
* [GeckoDriver](https://github.com/mozilla/geckodriver/)
