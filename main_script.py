import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre


DATA_BASE = 'sqlite:///./data/raw/raw_data_project_m1.db'

def argument_parser():
    parser = argparse.ArgumentParser(description='Group of people based on country and work')

    parser.add_argument('-c', '--country', type=str, help='Especify country you can need')
    parser.add_argument('-o', '--output', type=str, help='Especify path file')
    parser.add_argument('-d', '--data_base_path', type=str, help='Especify database path', default=DATA_BASE)

    args = parser.parse_args()
    print(args)

    return args


def main(multiple_args):
    country = multiple_args.country
    output = multiple_args.output
    data_base = multiple_args.data_base_path
    print('Starting pipeline...')
    country_info, career_info, jobs_title, country_tables = mac.acquire(data_base)
    print(country)

    normalize_df = mwr.wrangle(country_info, career_info, jobs_title, country_tables)

    result = man.analyze(normalize_df, country)

    if output:
        path = output
    else:
        if country:
            path = f'data/results/people_jobs_in_{country}.csv'
        else:
            path = 'data/results/people_jobs.csv'

    mre.report(result, path, normalize_df, 'adja.kane@cabify.com', path)


    print('pipeline finished...')


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)
