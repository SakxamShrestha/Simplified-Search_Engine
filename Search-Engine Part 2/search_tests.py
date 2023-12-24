from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############
    def test_search(self):
        programming_search_results = [['C Sharp (programming language)', 'Burna Boy', 1232492672, 52364], ['Python (programming language)', 'Burna Boy', 1137530195, 41571], ['Lua (programming language)', 'Burna Boy', 1113957128, 0], ['Covariance and contravariance (computer science)', 'Bearcat', 1167547364, 7453], ['Personal computer', 'Pegship', 1220391790, 45663], ['Ruby (programming language)', 'Bearcat', 1193928035, 30284]]
        self.assertEqual(search('programming'), programming_search_results)
        self.assertEqual(search(''), [])
        self.assertEqual(search('PrOgRaMmInG'), programming_search_results)

    def test_article_length(self):
        dog_search_metadata_results = [['Black dog (ghost)', 'Pegship', 1220471117, 14746], ['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138], ['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582], ['Guide dog', 'Jack Johnson', 1165601603, 7339], ['Sun dog', 'Mr Jake', 1208969289, 18050]]
        self.assertEqual(article_length(0, dog_search_metadata_results.copy()), [])
        self.assertEqual(article_length(3000, dog_search_metadata_results.copy()), [['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138]])
        self.assertEqual(article_length(-1000, dog_search_metadata_results.copy()), [])

        
    def test_unique_authors(self):
        music_search_metadata_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]        
        self.assertEqual(unique_authors(0, music_search_metadata_results.copy()), [])
        self.assertEqual(unique_authors(-1, music_search_metadata_results.copy()), [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755]])
        self.assertEqual(unique_authors(5, music_search_metadata_results.copy()), [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451]])
    
    def test_most_recent_article(self):
        soccer_search_metadata_results = [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]
        self.assertEqual(most_recent_article(soccer_search_metadata_results.copy()),  ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117])
        football_search_metadata_results = [['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718]]
        self.assertEqual(most_recent_article(football_search_metadata_results.copy()), [['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718]])

    def test_favorite_author(self):
        programming_search_metadata_results = [['C Sharp (programming language)', 'Burna Boy', 1232492672, 52364], ['Python (programming language)', 'Burna Boy', 1137530195, 41571], ['Lua (programming language)', 'Burna Boy', 1113957128, 0], ['Covariance and contravariance (computer science)', 'Bearcat', 1167547364, 7453], ['Personal computer', 'Pegship', 1220391790, 45663], ['Ruby (programming language)', 'Bearcat', 1193928035, 30284]]
        self.assertEqual(favorite_author('', programming_search_metadata_results.copy()), False)
        self.assertEqual(favorite_author('Bearcat', programming_search_metadata_results), True)
        self.assertEqual(favorite_author('Burna Boy', programming_search_metadata_results.copy()), True)    
 
    def test_title_and_author(self):
        computer_search_metadata_results = [['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144], ['Human computer', 'Bearcat', 1248275178, 4750], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Single-board computer', 'Gary King', 1220260601, 8271], ['Personal computer', 'Pegship', 1220391790, 45663], ['Digital photography', 'Mr Jake', 1095727840, 18093], ['Mode (computer interface)', 'Pegship', 1182732608, 2991]]
        self.assertEqual(title_and_author(computer_search_metadata_results.copy()), [('Ken Kennedy (computer scientist)', 'Mack Johnson'), ('Human computer', 'Bearcat'), ('List of dystopian music, TV programs, and games', 'Bearcat'), ('Single-board computer', 'Gary King'), ('Personal computer', 'Pegship'), ('Digital photography', 'Mr Jake'), ('Mode (computer interface)', 'Pegship')]) 
        self.assertEqual(title_and_author([]), [])

        soccer_search_metadata_results = [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]
        self.assertEqual(title_and_author(soccer_search_metadata_results.copy()), [('Spain national beach soccer team', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')])

    def test_refine_search(self):
        music_search_metadata_results = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        self.assertEqual(refine_search('guitar', music_search_metadata_results.copy()), [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718]])
        self.assertEqual(refine_search('', music_search_metadata_results.copy()), [])
        self.assertEqual(refine_search('PiAnO', music_search_metadata_results.copy()), [['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419]])
      
    #####################
    # INTEGRATION TESTS #
    #####################
    @patch('builtins.input')
    def test_advanced_unique_authors(self, input_mock):
        keyword = 'music'
        advanced_option = 2
        advanced_response = 10

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458]]\n"
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_most_recent_article(self, input_mock):
        keyword = 'soccer'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' +  "\nHere are your articles: ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_favorite_author(self, input_mock):
        keyword = 'music'
        advanced_option = 4
        advanced_response = 'Jack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]\nYour favorite author is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_title_and_author(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() +  str(advanced_option) + '\n' + "\nHere are your articles: [('Spain national beach soccer team', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('Steven Cohen (soccer)', 'Mack Johnson')]\n"

        self.assertEqual(output, expected) 


    @patch('builtins.input')
    def test_advanced_refine_search(self, input_mock):
        keyword = 'music'
        advanced_option = 6
        advanced_response = 'guitar'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Rock music', 'Mack Johnson', 1258069053, 119498], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718]]\n"
        self.assertEqual(output, expected) 


    @patch('builtins.input')
    def test_advanced_None(self, input_mock):
        keyword = 'time'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + "\nHere are your articles: [['Noise (music)', 'jack johnson', 1194207604, 15641], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['C Sharp (programming language)', 'Burna Boy', 1232492672, 52364], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['1936 in music', 'RussBot', 1243745950, 23417], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], ['Time travel', 'Jack Johnson', 1140826049, 35170], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['Python (programming language)', 'Burna Boy', 1137530195, 41571], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['Covariance and contravariance (computer science)', 'Bearcat', 1167547364, 7453], ['Personal computer', 'Pegship', 1220391790, 45663], ['Comparison of programming languages (basic instructions)', 'RussBot', 1238781354, 61644], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Ruby (programming language)', 'Bearcat', 1193928035, 30284], ['Semaphore (programming)', 'Nihonjoe', 1144850850, 7616]]\n"

        self.assertEqual(output, expected)  
     

               

               






            




# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
