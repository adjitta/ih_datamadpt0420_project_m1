import pandas as pd

import requests

from sqlalchemy import create_engine
from bs4 import BeautifulSoup

DATA_BASE = 'sqlite:///./data/raw/raw_data_project_m1.db'
API_URL = 'http://api.dataatwork.org/v1/jobs/autocomplete?contains=Data'
COUNTRY_CODES_URL = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'


def load_data(path):
    print('loading data')
    engine = create_engine(path)
    country_info = pd.read_sql_table(table_name='country_info', con=engine)
    career_info = pd.read_sql_table(table_name='career_info', con=engine)
    return country_info, career_info


def get_jobs_titles():
    response = requests.get(API_URL)
    result = response.json()
    jobs_title = pd.DataFrame(result)
    return jobs_title


def get_country_code_tables():
    country_code_page = requests.get(COUNTRY_CODES_URL)
    soup_country_code = BeautifulSoup(country_code_page.content, 'lxml')
    country_tables = soup_country_code.find_all('table')
    return country_tables


def acquire(path):
    country_info, career_info = load_data(path)
    jobs_title = get_jobs_titles()
    country_tables = get_country_code_tables()
    return country_info, career_info, jobs_title, country_tables
