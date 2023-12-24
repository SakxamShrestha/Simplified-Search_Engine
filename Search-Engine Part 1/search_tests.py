from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############
    def test_search(self):
        programming_search_results = ['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)']
        self.assertEqual(search('programming'), programming_search_results)
        self.assertEqual(search(''), [])
        self.assertEqual(search('PrOgRaMmInG'), programming_search_results)
        
    def test_title_length(self):
        time_search_results = ['Old-time music', 'Time travel', 'List of video games with time travel']
        self.assertEqual(title_length(0, time_search_results.copy()), [])
        self.assertEqual(title_length(25, time_search_results.copy()), ['Old-time music', 'Time travel']) 
        self.assertEqual(title_length(-1, time_search_results.copy()), [])

    def test_article_count(self):
        football_search_results = ['2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Georgia Bulldogs football under Robert Winston']
        self.assertEqual(article_count(2, football_search_results.copy()), ['2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football'])
        self.assertEqual(article_count(0, football_search_results.copy()), [])
        self.assertEqual(article_count(1, football_search_results.copy()), ['2009 Louisiana Tech Bulldogs football team'])

    def test_random_article(self):
        computer_search_results = ['Ken Kennedy (computer scientist)', 'Covariance and contravariance (computer science)', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']
        self.assertEqual(random_article(1, computer_search_results.copy()), 'Covariance and contravariance (computer science)')
        self.assertEqual(random_article(-1, computer_search_results.copy()), '')
        self.assertEqual(random_article(20, computer_search_results.copy()), '')


    def test_favorite_article(self):
        soccer_search_results = ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', "United States men's national soccer team 2009 results", 'China national soccer team', "Wake Forest Demon Deacons men's soccer"]
        self.assertEqual(favorite_article('', soccer_search_results.copy()), False)
        self.assertEqual(favorite_article('Football Club Barcelona', soccer_search_results.copy()), False)
        self.assertEqual(favorite_article('china National soccer Team', soccer_search_results.copy()), True)        
        
    def test_multiple_keywords(self):
        time_search_results = ['Old-time music', 'Time travel', 'List of video games with time travel']
        self.assertEqual(multiple_keywords('programming', time_search_results.copy()), ['Old-time music', 'Time travel', 'List of video games with time travel', 'C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)'])
        self.assertEqual(multiple_keywords('', time_search_results.copy()), ['Old-time music', 'Time travel', 'List of video games with time travel'])
        self.assertEqual(multiple_keywords('SocceR', time_search_results.copy()), ['Old-time music', 'Time travel', 'List of video games with time travel', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', "United States men's national soccer team 2009 results", 'China national soccer team', "Wake Forest Demon Deacons men's soccer"])


    #####################
    # INTEGRATION TESTS #
    #####################


    @patch('builtins.input')
    def test_advanced_title_length(self, input_mock):
        keyword = 'football'
        advanced_option = 1
        max_title_length = 25

        output = get_print(input_mock, [keyword, advanced_option, max_title_length])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(max_title_length)+ '\n' + "\nHere are your articles: ['Georgia Bulldogs football']\n"
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_article_count(self, input_mock):
        keyword = 'music'
        advanced_option = 2
        no_of_titles = 10

        output = get_print(input_mock, [keyword, advanced_option, no_of_titles])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(no_of_titles)+ '\n' + "\nHere are your articles: ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)']\n"
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_random_article(self, input_mock):
        keyword = 'soccer'
        advanced_option = 3
        article_index = 2

        output = get_print(input_mock, [keyword, advanced_option, article_index])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(article_index)+ '\n' + "\nHere are your articles: Steven Cohen (soccer)\n"
        self.assertEqual(output, expected) 

    @patch('builtins.input')
    def test_advanced_favorite_article(self, input_mock):
        keyword = 'programming'
        advanced_option = 4
        favorite_article = 'Lua (programming language)'

        output = get_print(input_mock, [keyword, advanced_option, favorite_article])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + favorite_article + '\n' + "\nHere are your articles: ['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)']\nYour favorite article is in the returned articles!\n"
        self.assertEqual(output, expected) 

    @patch('builtins.input')
    def test_advanced_multiple_keywords(self, input_mock):
        keyword = 'dog'
        advanced_option = 5
        other_keyword = 'programming'
        
        output = get_print(input_mock, [keyword, advanced_option, other_keyword])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + other_keyword + '\n' + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)']\n"
        self.assertEqual(output, expected)  


if __name__ == "__main__":
    main()
