from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_keyword_to_titles(self):
        metadata = []
        expected = {}
        self.assertEqual(keyword_to_titles(metadata), expected)

        metadata = [['1922 in music', 'Gary King', 1242717698, 11576, ['music', 'the', '1922', 'january', 'first', 'may', 'orchestra', 'radio', 'october', 'and', 'for', 'paul', 'walter', 'george', 'billy', 'harry', 'you', 'march', 'april', 'production', 'opened', 'theatre', 'september', 'ran', 'performances', 'august', 'american', 'singer', 'actress', 'composer', 'june']]]
        expected = {'music': ['1922 in music'], 'the': ['1922 in music'], '1922': ['1922 in music'], 'january': ['1922 in music'], 'first': ['1922 in music'], 'may': ['1922 in music'], 'orchestra': ['1922 in music'], 'radio': ['1922 in music'], 'october': ['1922 in music'], 'and': ['1922 in music'], 'for': ['1922 in music'], 'paul': ['1922 in music'], 'walter': ['1922 in music'], 'george': ['1922 in music'], 'billy': ['1922 in music'], 'harry': ['1922 in music'], 'you': ['1922 in music'], 'march': ['1922 in music'], 'april': ['1922 in music'], 'production': ['1922 in music'], 'opened': ['1922 in music'], 'theatre': ['1922 in music'], 'september': ['1922 in music'], 'ran': ['1922 in music'], 'performances': ['1922 in music'], 'august': ['1922 in music'], 'american': ['1922 in music'], 'singer': ['1922 in music'], 'actress': ['1922 in music'], 'composer': ['1922 in music'], 'june': ['1922 in music']} 
        self.assertEqual(keyword_to_titles(metadata), expected)

        metadata =  [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Noise (music)', 'jack johnson', 1194207604, 15641, ['noise', 'music', 'that', 'the', 'use', 'musical', 'this', 'made', 'and', 'sound', 'based', 'some', 'can', 'instruments', 'may', 'machine', 'sounds', 'audio', 'recordings', 'recording', 'other', 'produced', 'electronic', 'such', 'also', 'more', 'with', 'art', 'was', 'for', 'aesthetic', 'example', 'being', 'fluxus', 'artists', 'composition', 'early', 'young', 'rock', 'wave', 'industrial', 'works', 'his', 'from', 'one', 'not', 'signal', 'what', 'any', 'have', 'time', 'like', 'paul', 'hegarty', 'work', 'these', 'john', 'cage', 'which', 'all', 'japanese', 'genre', 'but', 'russolo', 'used', 'white', 'same', 'track', 'artist', 'first', 'had', 'found', 'called', 'created', 'paris', 'sirens', 'piece', 'using', 'percussion', 'tape', 'musique', 'concrète', 'group', 'recorded', 'various', '1960', 'album', 'cassette', 'ubuweb', 'com', 'ubu']]]
        expected = {'edogawa': ['Edogawa, Tokyo'], 'the': ['Edogawa, Tokyo', 'Noise (music)'], 'with': ['Edogawa, Tokyo', 'Noise (music)'], 'and': ['Edogawa, Tokyo', 'Noise (music)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'noise': ['Noise (music)'], 'music': ['Noise (music)'], 'that': ['Noise (music)'], 'use': ['Noise (music)'], 'musical': ['Noise (music)'], 'this': ['Noise (music)'], 'made': ['Noise (music)'], 'sound': ['Noise (music)'], 'based': ['Noise (music)'], 'some': ['Noise (music)'], 'can': ['Noise (music)'], 'instruments': ['Noise (music)'], 'may': ['Noise (music)'], 'machine': ['Noise (music)'], 'sounds': ['Noise (music)'], 'audio': ['Noise (music)'], 'recordings': ['Noise (music)'], 'recording': ['Noise (music)'], 'other': ['Noise (music)'], 'produced': ['Noise (music)'], 'electronic': ['Noise (music)'], 'such': ['Noise (music)'], 'also': ['Noise (music)'], 'more': ['Noise (music)'], 'art': ['Noise (music)'], 'was': ['Noise (music)'], 'for': ['Noise (music)'], 'aesthetic': ['Noise (music)'], 'example': ['Noise (music)'], 'being': ['Noise (music)'], 'fluxus': ['Noise (music)'], 'artists': ['Noise (music)'], 'composition': ['Noise (music)'], 'early': ['Noise (music)'], 'young': ['Noise (music)'], 'rock': ['Noise (music)'], 'wave': ['Noise (music)'], 'industrial': ['Noise (music)'], 'works': ['Noise (music)'], 'his': ['Noise (music)'], 'from': ['Noise (music)'], 'one': ['Noise (music)'], 'not': ['Noise (music)'], 'signal': ['Noise (music)'], 'what': ['Noise (music)'], 'any': ['Noise (music)'], 'have': ['Noise (music)'], 'time': ['Noise (music)'], 'like': ['Noise (music)'], 'paul': ['Noise (music)'], 'hegarty': ['Noise (music)'], 'work': ['Noise (music)'], 'these': ['Noise (music)'], 'john': ['Noise (music)'], 'cage': ['Noise (music)'], 'which': ['Noise (music)'], 'all': ['Noise (music)'], 'japanese': ['Noise (music)'], 'genre': ['Noise (music)'], 'but': ['Noise (music)'], 'russolo': ['Noise (music)'], 'used': ['Noise (music)'], 'white': ['Noise (music)'], 'same': ['Noise (music)'], 'track': ['Noise (music)'], 'artist': ['Noise (music)'], 'first': ['Noise (music)'], 'had': ['Noise (music)'], 'found': ['Noise (music)'], 'called': ['Noise (music)'], 'created': ['Noise (music)'], 'paris': ['Noise (music)'], 'sirens': ['Noise (music)'], 'piece': ['Noise (music)'], 'using': ['Noise (music)'], 'percussion': ['Noise (music)'], 'tape': ['Noise (music)'], 'musique': ['Noise (music)'], 'concrète': ['Noise (music)'], 'group': ['Noise (music)'], 'recorded': ['Noise (music)'], 'various': ['Noise (music)'], '1960': ['Noise (music)'], 'album': ['Noise (music)'], 'cassette': ['Noise (music)'], 'ubuweb': ['Noise (music)'], 'com': ['Noise (music)'], 'ubu': ['Noise (music)']}
        self.assertEqual(keyword_to_titles(metadata), expected)

    def test_title_to_info(self):
        metadata = []
        expected = {}
        self.assertEqual(title_to_info(metadata), expected)

        metadata =  [['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144, ['kennedy', 'was', 'computer', 'and', 'the', 'for', 'award']]]
        expected = {'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp': 1246308670, 'length': 4144}}
        self.assertEqual(title_to_info(metadata), expected)

        metadata =  [['Fiskerton, Lincolnshire', 'Bearcat', 1259869948, 5853, ['fiskerton', 'village', 'and', 'the', 'was', 'which', 'that', 'been']], ['Reflection-oriented programming', 'Nihonjoe', 1143366937, 38, []], ['B (programming language)', 'jack johnson', 1196622610, 5482, ['language', 'the', 'thompson', 'ritchie', 'was', 'from', 'bcpl', 'and', 'that', 'for', 'pdp', 'version', 'this']]]
        expected =  {'Fiskerton, Lincolnshire': {'author': 'Bearcat', 'timestamp': 1259869948, 'length': 5853}, 'Reflection-oriented programming': {'author': 'Nihonjoe', 'timestamp': 1143366937, 'length': 38}, 'B (programming language)': {'author': 'jack johnson', 'timestamp': 1196622610, 'length': 5482}}
        self.assertEqual(title_to_info(metadata), expected)

    def test_search(self):
        keyword_to_titles = {}
        keyword = ''
        expected = []
        self.assertEqual(search(keyword, keyword_to_titles), expected)

        keyword_to_titles = {'edogawa': ['Edogawa, Tokyo'], 'the': ['Edogawa, Tokyo', 'Noise (music)'], 'with': ['Edogawa, Tokyo', 'Noise (music)'], 'and': ['Edogawa, Tokyo', 'Noise (music)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'noise': ['Noise (music)'], 'music': ['Noise (music)'], 'that': ['Noise (music)'], 'use': ['Noise (music)'], 'musical': ['Noise (music)'], 'this': ['Noise (music)'], 'made': ['Noise (music)'], 'sound': ['Noise (music)'], 'based': ['Noise (music)'], 'some': ['Noise (music)'], 'can': ['Noise (music)'], 'instruments': ['Noise (music)'], 'may': ['Noise (music)'], 'machine': ['Noise (music)'], 'sounds': ['Noise (music)'], 'audio': ['Noise (music)'], 'recordings': ['Noise (music)'], 'recording': ['Noise (music)'], 'other': ['Noise (music)'], 'produced': ['Noise (music)'], 'electronic': ['Noise (music)'], 'such': ['Noise (music)'], 'also': ['Noise (music)'], 'more': ['Noise (music)'], 'art': ['Noise (music)'], 'was': ['Noise (music)'], 'for': ['Noise (music)'], 'aesthetic': ['Noise (music)'], 'example': ['Noise (music)'], 'being': ['Noise (music)'], 'fluxus': ['Noise (music)'], 'artists': ['Noise (music)'], 'composition': ['Noise (music)'], 'early': ['Noise (music)'], 'young': ['Noise (music)'], 'rock': ['Noise (music)'], 'wave': ['Noise (music)'], 'industrial': ['Noise (music)'], 'works': ['Noise (music)'], 'his': ['Noise (music)'], 'from': ['Noise (music)'], 'one': ['Noise (music)'], 'not': ['Noise (music)'], 'signal': ['Noise (music)'], 'what': ['Noise (music)'], 'any': ['Noise (music)'], 'have': ['Noise (music)'], 'time': ['Noise (music)'], 'like': ['Noise (music)'], 'paul': ['Noise (music)'], 'hegarty': ['Noise (music)'], 'work': ['Noise (music)'], 'these': ['Noise (music)'], 'john': ['Noise (music)'], 'cage': ['Noise (music)'], 'which': ['Noise (music)'], 'all': ['Noise (music)'], 'japanese': ['Noise (music)'], 'genre': ['Noise (music)'], 'but': ['Noise (music)'], 'russolo': ['Noise (music)'], 'used': ['Noise (music)'], 'white': ['Noise (music)'], 'same': ['Noise (music)'], 'track': ['Noise (music)'], 'artist': ['Noise (music)'], 'first': ['Noise (music)'], 'had': ['Noise (music)'], 'found': ['Noise (music)'], 'called': ['Noise (music)'], 'created': ['Noise (music)'], 'paris': ['Noise (music)'], 'sirens': ['Noise (music)'], 'piece': ['Noise (music)'], 'using': ['Noise (music)'], 'percussion': ['Noise (music)'], 'tape': ['Noise (music)'], 'musique': ['Noise (music)'], 'concrète': ['Noise (music)'], 'group': ['Noise (music)'], 'recorded': ['Noise (music)'], 'various': ['Noise (music)'], '1960': ['Noise (music)'], 'album': ['Noise (music)'], 'cassette': ['Noise (music)'], 'ubuweb': ['Noise (music)'], 'com': ['Noise (music)'], 'ubu': ['Noise (music)']}
        keyword = 'the' 
        expected = ['Edogawa, Tokyo', 'Noise (music)']
        self.assertEqual(search(keyword, keyword_to_titles), expected)

        keyword_to_titles = {'music': ['1922 in music'], 'the': ['1922 in music'], '1922': ['1922 in music'], 'january': ['1922 in music'], 'first': ['1922 in music'], 'may': ['1922 in music'], 'orchestra': ['1922 in music'], 'radio': ['1922 in music'], 'october': ['1922 in music'], 'and': ['1922 in music'], 'for': ['1922 in music'], 'paul': ['1922 in music'], 'walter': ['1922 in music'], 'george': ['1922 in music'], 'billy': ['1922 in music'], 'harry': ['1922 in music'], 'you': ['1922 in music'], 'march': ['1922 in music'], 'april': ['1922 in music'], 'production': ['1922 in music'], 'opened': ['1922 in music'], 'theatre': ['1922 in music'], 'september': ['1922 in music'], 'ran': ['1922 in music'], 'performances': ['1922 in music'], 'august': ['1922 in music'], 'american': ['1922 in music'], 'singer': ['1922 in music'], 'actress': ['1922 in music'], 'composer': ['1922 in music'], 'june': ['1922 in music']}
        keyword = 'lorumipsum' 
        expected = []
        self.assertEqual(search(keyword, keyword_to_titles), expected)

    def test_article_length(self):
        article_titles = ['Lights (musician)', 'List of soul musicians']
        title_to_info = {
            'Lights (musician)': {
                'author': 'Burna Boy',
                'timestamp':  1213914297,
                'length': 5898
            },

            'List of soul musicians': {
                'author': 'jack johnson',
                'timestamp': 1175455921, 
                'length': 4878
            }
        }         

        expected = []
        self.assertEqual(article_length(1000, [], title_to_info), [])
        self.assertEqual(article_length(5000, article_titles, title_to_info), ['List of soul musicians'])
        self.assertEqual(article_length(10000, article_titles, title_to_info), ['Lights (musician)', 'List of soul musicians'])

          
    def test_key_to_author(self):
        titles = ['Lights (musician)', 'List of soul musicians']
        title_to_info = {
            'Lights (musician)': {
                'author': 'Burna Boy',
                'timestamp':  1213914297,
                'length': 5898
            },

            'List of soul musicians': {
                'author': 'jack johnson',
                'timestamp': 1175455921, 
                'length': 4878
            }
        }         
        expected = {
            'Burna Boy': ['Lights (musician)'],
            'jack johnson': ['List of soul musicians']
        }
        
        self.assertEqual(key_by_author(titles, title_to_info), expected)

        titles = ['title1', 'title2']
        title_to_info = {
            'title1': {
                'author': 'author1',
                'timestamp':  'timestamp1',
                'length': 'article_length1'
            },

            'title2': {
                'author': 'author2',
                'timestamp': 'timestamp2', 
                'length': 'article_length2'
            }
        }         
        expected = {
            'author1': ['title1'],
            'author2': ['title2']
        }
        self.assertEqual(key_by_author(titles, title_to_info), expected)

        self.assertEqual(key_by_author([], {}), {})
    
    def test_filter_to_author(self):
        # 'Burna Boy': ['Lights (musician)'],
        #     'jack johnson': ['List of soul musicians']
        author = 'Burna Boy'
        titles = ['Lights (musician)', 'List of soul musicians']
        title_to_info = {
            'Lights (musician)': {
                'author': 'Burna Boy',
                'timestamp':  1213914297,
                'length': 5898
            },

            'List of soul musicians': {
                'author': 'jack johnson',
                'timestamp': 1175455921, 
                'length': 4878
            }
        }
        expected = ['Lights (musician)']
        self.assertEqual(filter_to_author(author, titles, title_to_info), expected)

        author = 'jack johnson'
        expected = ['List of soul musicians']
        self.assertEqual(filter_to_author(author, titles, title_to_info), expected)

        author = ''
        expected = []
        self.assertEqual(filter_to_author(author, titles, title_to_info), expected)


    def test_filter_out(self):
        keyword_to_titles = {} 
        expected = ['2009 in music', 'Spain national beach soccer team']
        self.assertEqual(filter_out('hot', ['2009 in music', 'Spain national beach soccer team'], keyword_to_titles), expected)

        keyword_to_titles = {'the': ['The Mandogs', 'David Levi (musician)', 'Scores (computer virus)'], 'mandogs': ['The Mandogs'], 'was': ['The Mandogs'], 'show': ['The Mandogs'], 'hosts': ['The Mandogs'], 'and': ['The Mandogs', 'Scores (computer virus)'], '2012': ['The Mandogs'], 'for': ['The Mandogs'], 'has': ['The Mandogs'], 'other': ['The Mandogs'], 'his': ['The Mandogs'], 'jay': ['The Mandogs'], 'naked': ['David Levi (musician)'], 'brothers': ['David Levi (musician)'], 'band': ['David Levi (musician)'], 'scores': ['Scores (computer virus)'], 'virus': ['Scores (computer virus)'], '1988': ['Scores (computer virus)'], 'system': ['Scores (computer virus)']}
        expected = []
        self.assertEqual(filter_out('lorem', [], keyword_to_titles), expected)

        keyword_to_titles = {'edogawa': ['Edogawa, Tokyo'], 'the': ['Edogawa, Tokyo', 'Noise (music)'], 'with': ['Edogawa, Tokyo', 'Noise (music)'], 'and': ['Edogawa, Tokyo', 'Noise (music)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'noise': ['Noise (music)'], 'music': ['Noise (music)'], 'that': ['Noise (music)'], 'use': ['Noise (music)'], 'musical': ['Noise (music)'], 'this': ['Noise (music)'], 'made': ['Noise (music)'], 'sound': ['Noise (music)'], 'based': ['Noise (music)'], 'some': ['Noise (music)'], 'can': ['Noise (music)'], 'instruments': ['Noise (music)'], 'may': ['Noise (music)'], 'machine': ['Noise (music)'], 'sounds': ['Noise (music)'], 'audio': ['Noise (music)'], 'recordings': ['Noise (music)'], 'recording': ['Noise (music)'], 'other': ['Noise (music)'], 'produced': ['Noise (music)'], 'electronic': ['Noise (music)'], 'such': ['Noise (music)'], 'also': ['Noise (music)'], 'more': ['Noise (music)'], 'art': ['Noise (music)'], 'was': ['Noise (music)'], 'for': ['Noise (music)'], 'aesthetic': ['Noise (music)'], 'example': ['Noise (music)'], 'being': ['Noise (music)'], 'fluxus': ['Noise (music)'], 'artists': ['Noise (music)'], 'composition': ['Noise (music)'], 'early': ['Noise (music)'], 'young': ['Noise (music)'], 'rock': ['Noise (music)'], 'wave': ['Noise (music)'], 'industrial': ['Noise (music)'], 'works': ['Noise (music)'], 'his': ['Noise (music)'], 'from': ['Noise (music)'], 'one': ['Noise (music)'], 'not': ['Noise (music)'], 'signal': ['Noise (music)'], 'what': ['Noise (music)'], 'any': ['Noise (music)'], 'have': ['Noise (music)'], 'time': ['Noise (music)'], 'like': ['Noise (music)'], 'paul': ['Noise (music)'], 'hegarty': ['Noise (music)'], 'work': ['Noise (music)'], 'these': ['Noise (music)'], 'john': ['Noise (music)'], 'cage': ['Noise (music)'], 'which': ['Noise (music)'], 'all': ['Noise (music)'], 'japanese': ['Noise (music)'], 'genre': ['Noise (music)'], 'but': ['Noise (music)'], 'russolo': ['Noise (music)'], 'used': ['Noise (music)'], 'white': ['Noise (music)'], 'same': ['Noise (music)'], 'track': ['Noise (music)'], 'artist': ['Noise (music)'], 'first': ['Noise (music)'], 'had': ['Noise (music)'], 'found': ['Noise (music)'], 'called': ['Noise (music)'], 'created': ['Noise (music)'], 'paris': ['Noise (music)'], 'sirens': ['Noise (music)'], 'piece': ['Noise (music)'], 'using': ['Noise (music)'], 'percussion': ['Noise (music)'], 'tape': ['Noise (music)'], 'musique': ['Noise (music)'], 'concrète': ['Noise (music)'], 'group': ['Noise (music)'], 'recorded': ['Noise (music)'], 'various': ['Noise (music)'], '1960': ['Noise (music)'], 'album': ['Noise (music)'], 'cassette': ['Noise (music)'], 'ubuweb': ['Noise (music)'], 'com': ['Noise (music)'], 'ubu': ['Noise (music)']} 
        expected =  ['Edogawa, Tokyo', '1922 in music']
        self.assertEqual(filter_out('',  ['Edogawa, Tokyo', '1922 in music'], keyword_to_titles), expected)


    def test_articles_from_year(self):
        title_to_info = {'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, '1962 in country music': {'author': 'Mack Johnson', 'timestamp': 1249862464, 'length': 7954}}
        expected = []
        self.assertEqual(articles_from_year(2000, ['Edogawa, Tokyo', '1922 in music'], title_to_info), expected)

        title_to_info =  {'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp': 1246308670, 'length': 4144}, 'Reflection-oriented programming': {'author': 'Nihonjoe', 'timestamp': 1143366937, 'length': 38}, 'B (programming language)': {'author': 'jack johnson', 'timestamp': 1196622610, 'length': 5482}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, '1962 in country music': {'author': 'Mack Johnson', 'timestamp': 1249862464, 'length': 7954}}
        expected = ['Ken Kennedy (computer scientist)']
        self.assertEqual(articles_from_year(2009, ['Ken Kennedy (computer scientist)', '2009 in music', 'Spain national beach soccer team', 'Reflection-oriented programming'], title_to_info), expected)


        title_to_info = {}
        expected =  []
        self.assertEqual(articles_from_year(2004, ['Edogawa, Tokyo', '1922 in music'], title_to_info), expected)                      

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_article_length_integration_test(self, input_mock):
        keyword = 'music'
        advanced_option = 1
        advanced_response = 5050

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Kevin Cadogan', 'Tim Arnold (musician)', 'List of gospel musicians', 'Texture (music)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_key_by_author_integration_test(self, input_mock):
        keyword = 'black'
        advanced_option = 2
         
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: {'RussBot': ['2009 in music', 'Fisk University'], 'Mack Johnson': ['Rock music'], 'Pegship': ['Black dog (ghost)'], 'Bearcat': ['List of dystopian music, TV programs, and games', 'Landseer (dog)'], 'Burna Boy': ['Georgia Bulldogs football']}\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_filter_to_author_integration_test(self, input_mock):
        keyword = 'the'
        advanced_option = 3
        advanced_response = 'jack johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Noise (music)', '1986 in music', 'List of soul musicians', 'USC Trojans volleyball', 'Tim Arnold (musician)', 'B (programming language)', 'David Gray (musician)', 'Alex Turner (musician)', 'George Crum (musician)', 'Spawning (computer gaming)']\n"
        
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_filter_out_integration_test(self, input_mock):
        keyword = 'music'
        advanced_option = 4
        advanced_response = 'artists'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['List of Canadian musicians', 'French pop music', '1922 in music', '1986 in music', 'Kevin Cadogan', '2009 in music', 'Lights (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Joe Becker (musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', '1996 in music', 'Traditional Thai musical instruments', '2006 in music', 'Texture (music)', '2007 in music', '2008 in music']\n"

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_articles_from_year_integration_test(self, input_mock):
        keyword = 'all'
        advanced_option = 5
        advanced_response = 2008

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Arabic music', 'Annie (musical)', 'Personal computer', 'Sean Delaney (musician)']\n"  

        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_None_integration_test(self, input_mock):
        keyword = 'book'
        advanced_option = 6
        
        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['List of dystopian music, TV programs, and games', 'Annie (musical)']\n"

        self.assertEqual(output, expected) 

if __name__ == "__main__":
    main()
