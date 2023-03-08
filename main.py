import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None

    def _send_request(self):
        try:
            self.response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
            return False
        return True

    def _parse_html(self):
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def get_links(self):
        pass

    def get_title(self):
        pass

    def get_images(self):
        pass

    def get_headings(self):
        if not self._send_request():
            return
        self._parse_html()
        headings = []
        for heading in self.soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            headings.append(heading.text.strip())
        return headings

    def get_paragraphs(self):
        pass

    def get_metadata(self):
        if not self._send_request():
            return
        self._parse_html()
        meta_data = {}
        for meta in self.soup.find_all('meta'):
            if meta.get('name'):
                meta_data[meta.get('name')] = meta.get('content')
            elif meta.get('property'):
                meta_data[meta.get('property')] = meta.get('content')
        return meta_data

udemy=WebScraper("https://www.udemy.com/")
print(udemy.get_paragraphs())