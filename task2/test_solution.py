import unittest

import solution


class TestCountingAnimals(unittest.TestCase):
    def setUp(self):
        solution.animals_dict.clear()
        self.url_two_letters = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pageuntil=%D0%91%D0%B0%D1%80%D0%B1%D1%83%D1%81-%D0%BE%D0%BB%D0%B8%D0%B3%D0%BE%D0%BB%D0%B5%D0%BF%D0%B8%D1%81#mw-pages"

    def test_count_animals_on_page_two_letters_correct(self):
        solution.count_animals_on_page(self.url_two_letters)
        self.assertEqual(solution.animals_dict, {"А": 98, "Б": 102})

    def test_count_animals_on_page_two_letters_incorrect(self):
        solution.count_animals_on_page(self.url_two_letters)
        self.assertNotEqual(solution.animals_dict, {"А": 98, "Б": 101})


if __name__ == "__main__":
    unittest.main()
