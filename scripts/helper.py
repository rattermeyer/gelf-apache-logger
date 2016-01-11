import unittest
import re

class TestTemplateExtractor(unittest.TestCase):
    def template_extractor(self, url):
        normalized = re.sub(r'[a-fA-F0-9]{32}', '_', url)
        return re.sub(r'\/_$', '', normalized)

    def test_replaces_uids(self):
        url = '/hello/24F6951556A945EE9E3A495B8783D7A8/world/24F6951556A945EE9E3A495B8783D7A8'
        self.assertEqual(self.template_extractor(url), '/hello/_/world')

if __name__ == '__main__':
    unittest.main()