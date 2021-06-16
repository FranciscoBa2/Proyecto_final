import requests
def consulta_libros_nyt_fict(url):
        params = {'api-key': 'mllWj4Wcwtr86SFL1XJjbnVLyv71Nf1m'}
        response = requests.get(url, params)
        if response.status_code == 200:
                print('ok')
        else:
                print('not ok')
        contenido = response.json()['results']['books']
        for n in contenido:
            print('Rank:', n['rank'], ' Title:', n['title'], ' Author:',
                  n['author'], ' Description:', n['description'])


# #
def consulta_libros_nyt_nonfict(url):
        params = {'api-key': 'mllWj4Wcwtr86SFL1XJjbnVLyv71Nf1m'}
        response = requests.get(url, params)
        if response.status_code == 200:
                print('ok')
        else:
                print('not ok')
        contenido = response.json()['results']['books']
        for n in contenido:
                print('Rank:', n['rank'], ' Title:', n['title'], ' Author:',
                      n['author'], ' Description:', n['description'])


"""
para_sacar_apis = 'https://github.com/public-apis/public-apis'
documentacion = 'https://docs.python-requests.org/en/master/'
para_entender_contenido = 'http://json.parser.online.fr/'

"""
