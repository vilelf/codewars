from unittest import TestCase
from breaking_search_bad.main import search


class MainTest(TestCase):
    def test_main(self):
        titles = [
            'The Big Bang Theory',
            'How I Met Your Mother',
            'Dexter',
            'Breaking Bad',
            'Doctor Who',
            'The Hobbit',
            'Pacific Rim',
            'Pulp Fiction',
            'The Avengers',
            'Shining'
        ]
        self.assertEqual(search(titles, 'ho'), ['How I Met Your Mother', 'Doctor Who', 'The Hobbit'])
        self.assertEqual(search(titles, 'exte'), ['Dexter'])
        self.assertEqual(search(titles, 'the'), ['The Big Bang Theory', 'How I Met Your Mother', 'The Hobbit', 'The Avengers'])	