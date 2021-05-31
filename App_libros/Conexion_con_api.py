import requests
def consulta_libros_nyt(url, title):
        params = {'api-key': 'mllWj4Wcwtr86SFL1XJjbnVLyv71Nf1m'}
        response = requests.get(url, params)
        if response.status_code == 200:
                print('ok')
        else:
                print('not ok')
        contenido = response.json()['results']['books']
        for n in contenido:
            if n['title'] == title:
                    print('Rank:', n['rank'], ' Title:', n['title'], ' Author:', n['author'], ' Description:', n['description'])
consulta_libros_nyt(url='https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json', title='WHILE JUSTICE SLEEPS')
#
# """title='WHILE JUSTICE SLEEPS'

# #
# def consulta_libros_nyt(url, title):
#         params = {'api-key': 'mllWj4Wcwtr86SFL1XJjbnVLyv71Nf1m', 'publication_dt': '2021-05-11'}
#         response = requests.get(url, params)
#         if response.status_code == 200:
#                 print('ok')
#         else:
#                 print('not ok')
#         contenido = response.json()['results']['books']
#         for n in contenido:
#                 if n['title'] == title:
#                         print('Rank:', n['rank'], ' Title:', n['title'], ' Author:', n['author'], ' Description:', n['description'])
#
# consulta_libros_nyt(url='https://api.nytimes.com/svc/books/v3/lists/current/paperback-nonfiction.json', title='JUST MERCY')

"""
para_sacar_apis = 'https://github.com/public-apis/public-apis'
documentacion = 'https://docs.python-requests.org/en/master/'
para_entender_contenido = 'http://json.parser.online.fr/'

Fiction:

SOOLEY
THE LAST THING HE TOLD ME
PROJECT HAIL MARY
WHILE JUSTICE SLEEPS
21ST BIRTHDAY
THE HILL WE CLIMB
THE MIDNIGHT LIBRARY
THAT SUMMER
THE FOUR WINDS
A GAMBLING MAN
THE INVISIBLE LIFE OF ADDIE LARUE
THE DEVIL MAY DANCE
THE PLOT
WHERE THE GRASS IS GREEN AND THE GIRLS ARE PRETTY
FINDING ASHLEY


Non-fiction:

THE BODY KEEPS THE SCORE
JUST MERCY
WHITE FRAGILITY
BORN A CRIME
BECOMING
KILLERS OF THE FLOWER MOON
THINKING, FAST AND SLOW
SAPIENS
NOMADLAND
BRAIDING SWEETGRASS
COUNTDOWN 1945
MY GRANDMOTHER'S HANDS
THE WARMTH OF OTHER SUNS
OUTLIERS
THE HUNDRED YEARS' WAR ON PALESTINE
"""
