import json
from urllib import urlopen


def getVacancies(query, page=0):
    response = urlopen("https://api.hh.ru/vacancies/"+query+'&page='+str(page)).read()
    responseJson = json.loads(response)

    for vacancy in responseJson['items']:
        print(vacancy.get('id', ''))

    if responseJson['pages'] > page:
        page = page + 1
        getVacancies('?text=%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F+%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C&enable_snippets=false&area=2', page)
    else:
        return(responseJson['pages'])


getVacancies('?text=%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F+%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C&enable_snippets=false&area=2')
