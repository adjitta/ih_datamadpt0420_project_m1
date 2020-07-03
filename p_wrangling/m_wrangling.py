import pandas as pd


def clean_scrapped_data(country_tables):
    print('Cleaning scrapped data...')

    country_table_text = []
    for country in country_tables:
        country_table_text.append(country.text)

    country_table_split = list(map(lambda x: x.split('\n'), country_table_text))

    country_split = []
    for country in country_table_split:
        for country_code in country:
            if (country_code != '') and (country_code != '\xa0') and (country_code != ' \xa0'):
                country_split.append(country_code)

    row_split = 2
    rows_refactored = [country_split[x:x + row_split] for x in range(0, len(country_split), row_split)]
    rows_refactored

    country_code_df = pd.DataFrame(rows_refactored, columns=['country', 'country_code'])
    country_code_df['country_code'] = country_code_df['country_code'].str.replace('(', '')
    country_code_df['country_code'] = country_code_df['country_code'].str.replace(')', '')
    country_code_df.replace(to_replace=["EL"], value=["GR"], inplace=True)
    country_code_df['country_code'] = country_code_df['country_code'].str.replace('UK', 'GB')
    return country_code_df


def merge_data(country_info, country_code_df, career_info, jobs_title):
    print('Merging data...')

    country_code_merge = country_info.merge(country_code_df,
                                            how='inner',
                                            left_on='country_code',
                                            right_on='country_code')
    career_merge = country_code_merge.merge(career_info,
                                            how='left',
                                            left_on='uuid',
                                            right_on='uuid')
    data_merged = career_merge.merge(jobs_title,
                                     how='left',
                                     left_on='normalized_job_code',
                                     right_on='uuid')
    return data_merged[['uuid_x',
                        'country',
                        'dem_education_level',
                        'dem_full_time_job',
                        'normalized_job_title',
                        'rural']]


def normalize_data(data):
    print('Normalizing data...')

    data['rural'] = data['rural'].str.replace('city', 'urban')
    data['rural'] = data['rural'].str.replace('Non-Rural', 'urban')
    data['rural'] = data['rural'].str.replace('Country', 'rural')
    data['rural'] = data['rural'].str.replace('countryside', 'rural')
    # data['Job Title'] = data['Job Title'].fillna('No work')

    data.rename(columns={'uuid_x': 'ID',
                         'dem_education_level': 'Education level',
                         'dem_full_time_job': 'Full time job',
                         'normalized_job_title': 'Job Title',
                         'rural': 'Lifestyle'},
                inplace=True)
    return data


def wrangle(country_info, career_info, jobs_title, country_tables):
    country_code_df = clean_scrapped_data(country_tables)
    merged_data = merge_data(country_info, country_code_df, career_info, jobs_title)
    return normalize_data(merged_data)
