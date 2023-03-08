import unittest
from main import WebScraper


class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.udemy.com/'
        self.web_scraper = WebScraper(self.url)

    def test_get_links(self):
        links = self.web_scraper.get_links()
        self.assertTrue(len(links) > 0)
        self.assertIsInstance(links, list)
        self.assertTrue(all(isinstance(link, str) for link in links))

    def test_get_title(self):
        title = self.web_scraper.get_title()
        self.assertTrue(len(title) > 0)
        self.assertIsInstance(title, str)

    def test_get_images(self):
        images = self.web_scraper.get_images()
        self.assertTrue(len(images) > 0)
        self.assertIsInstance(images, list)
        self.assertTrue(all(isinstance(image, str) for image in images))

    def test_get_headings(self):
        headings = self.web_scraper.get_headings()
        self.assertTrue(len(headings) > 0)
        self.assertIsInstance(headings, list)
        self.assertTrue(all(isinstance(heading, str) for heading in headings))

    def test_get_paragraphs(self):
        paragraphs = self.web_scraper.get_paragraphs()
        self.assertTrue(len(paragraphs) > 0)
        self.assertIsInstance(paragraphs, list)
        self.assertTrue(all(isinstance(paragraph, str) for paragraph in paragraphs))

    def test_get_metadata(self):
        metadata = self.web_scraper.get_metadata()
        self.assertTrue(len(metadata) > 0)
        self.assertIsInstance(metadata, dict)
        self.assertTrue(all(isinstance(key, str) for key in metadata.keys()))
        self.assertTrue(all(isinstance(value, str) for value in metadata.values()))


if __name__ == '__main__':
    unittest.main()
