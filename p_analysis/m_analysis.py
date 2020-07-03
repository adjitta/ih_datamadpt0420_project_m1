def group_data(data):
    print('start with analysis')
    grouped = data.groupby(['country', 'Job Title', 'Lifestyle']).agg({'ID': 'count'})
    grouped.columns = ['Quantity']
    grouped = grouped.reset_index()
    grouped['Percentage'] = (grouped['Quantity'] / grouped['Quantity'].sum()) * 100
    grouped['Percentage'] = grouped['Percentage'].apply(lambda x: "{0:.2f}%".format(x))
    grouped['Job Title'] = grouped['Job Title'].apply(lambda x: x.capitalize())
    grouped.sort_values(by='Quantity', ascending=False)
    return grouped


def filter_by_country(df, country):
    if country is not None:
        return df[df['country'] == country]
    else:
        return df




def analyze(data, country):
    df = group_data(data)
    return filter_by_country(df, country)
