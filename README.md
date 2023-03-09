# Web Scraper

Web scraping is the process of extracting data from websites. In this project, you will write a web scraper that extracts information from a webpage using Python. Some real-life examples of web scraping include price comparison websites, stock market analysis, and social media sentiment analysis.

In this project, you will use the requests and BeautifulSoup libraries to send a request to a webpage, parse the HTML content, and extract useful information.

## Your Task
Your task is to implement the WebScraper class in main.py. This class should have the following methods:

get_links: This method should return a list of all the links on the webpage.

get_title: This method should return the title of the webpage.

get_images: This method should return a list of all the images on the webpage.

get_headings: This method should return a list of all the headings (h1-h6) on the webpage.

get_paragraphs: This method should return a list of all the paragraphs on the webpage.

get_metadata: This method should return a dictionary of all the metadata on the webpage.

You will need to fill in the code for each of the methods that has a 'TODO' string.
The following methods are incomplete:

1. get_links(self)
2. get_title(self):
3. get_images(self)
4. get_paragraphs(self)


 We have already provided the _send_request and _parse_html methods to help you send a request to the webpage and parse the HTML content.

## How to Use
You can create a WebScraper object by passing in the URL of the webpage you want to scrape. For example:

udemy = WebScraper("https://www.udemy.com/")
You can then call any of the methods on the WebScraper object to extract information from the webpage. For example:


links = udemy.get_links()

title = udemy.get_title()

images = udemy.get_images()

headings = udemy.get_headings()

paragraphs = udemy.get_paragraphs()

metadata = udemy.get_metadata()

##Testing
We have provided a set of unit tests in test_main.py. You can run these tests by running python -m test_main in the terminal.

Your task is to write the code for the methods in main.py so that all of the tests pass.

We have also provided two screenshots in the tests folder: passed.png and failed.png. If all of the tests pass, your output should look like the passed.png screenshot. If any of the tests fail, your output will look like the failed.png screenshot.

Submitting Your Solution
Please submit your solution as a zip file containing your main.py file.
