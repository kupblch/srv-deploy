import time
import json
from urllib import urlopen
from datetime import datetime


def getVacancies(query, page=0):
    t0 = time.clock()
    response = urlopen("https://api.hh.ru/vacancies/"+query+'&page='+str(page)).read()
    responseJson = json.loads(response)
    if (time.clock() - t0) < 1:
        time.sleep(1 - (time.clock() - t0))

    for vacancy in responseJson['items']:
        ids.append(vacancy.get('id', '').encode('utf-8'))

    if responseJson['pages'] > page:
        page = page + 1
        getVacancies(query, page)
    else:
        return(ids)

ids=[]
getVacancies('?text=%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F+%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C&enable_snippets=false&area=2')

print(len(ids))
print(ids)
