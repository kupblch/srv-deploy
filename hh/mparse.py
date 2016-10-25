import sys
import requests
import json
import csv
import re

reload(sys)
sys.setdefaultencoding('utf8')
out_csv = sys.argv[1]
text = sys.argv[2]
area = sys.argv[3]


api_url = "https://api.hh.ru"
query = "/vacancies?area=%s&text=%s" %(area, text)

def removeTag(soup=''):
    if soup is not None:
        return re.sub('<[^>]*>', '', soup)
    else:
        return ''


def search(text, page=0):
    _url = '%s%s&page=%s' % (api_url, query, page)
    print _url
    r = requests.get(_url)

    result = json.loads(r.content)

    pages = result['pages']
    page = result['page']
    parse(result)
#    print json.dumps(result, sort_keys=True, indent=4)

    if page < pages:
        search(text, page+1)

def parse(result):
    if not result['items']:
        return
    for vacancy in result['items']:
#         print json.dumps(vacancy, sort_keys=True, indent=4)
        vacancy_id = vacancy.get('id', '')
        url = vacancy.get('alternate_url', '')
        created_at = vacancy.get('created_at', '')
        published_at = vacancy.get('published_at', '')
        name = vacancy.get('name', '')
        premium = vacancy.get('premium', '')
        if vacancy['salary']:
            salary_currency = vacancy['salary']['currency']
            salary_from = vacancy['salary']['from']
            salary_to = vacancy['salary']['to']
        else:
            salary_currency = None
            salary_from = None
            salary_to = None
        snippet_requirement = removeTag( vacancy['snippet'].get('requirement', '') )
        snippet_responsibility = removeTag( vacancy['snippet'].get( 'requirement', ''))
        employer_name = vacancy['employer'].get('name', '')
        employer_id = vacancy['employer'].get('id', '')
        vacancy_type = vacancy['type'].get('id', '')
        writer.writerow( (vacancy_id, url, name, employer_name, salary_currency, salary_from, salary_to, snippet_requirement, snippet_responsibility, employer_id, vacancy_type, premium, created_at, published_at) )


csv_file = open(out_csv, 'wt')
writer =  csv.writer(csv_file, delimiter ='\t')
writer.writerow( ('vacancy_id', 'url', 'name', 'employer_name', 'salary_currency', 'salary_from', 'salary_to', 'snippet_requirement', 'snippet_responsibility', 'employer_id', 'vacancy_type', 'premium', 'created_at', 'published_at') )


search(text)
