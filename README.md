# Does lifestyle influence the type of work?

With this project we intend to group the jobs of people according to their job title, country and lifestyle (urban or rural).
Remember to change branches: my-first-project.


![Image](https://images.unsplash.com/photo-1532214950507-92ba44a2f6f7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80)

---
### Data sources :
 - Database with the job codes and the demographic information
    - Provided by [Ironhack](http://www.potacho.com/files/ironhack/raw_data_project_m1.db) formatted as a `.db` file.
 - API access to Swagger data created by [Work Data Initiative](http://api.dataatwork.org/v1/jobs/autocomplete?contains=data
 )
 - Scraping the country codes from [Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes)

## **Installation**
Use the package manager conda to install the following libraries:

```bash
conda install pandas
conda install sqlalchemy
conda install requests
conda instal Seaborn
conda install Matplotlib
```
###  **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   ├── notebook1.ipynb
    │   └── notebook2.ipynb
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── data
        ├── raw
        ├── processed
        └── results
```
###Country analysis :
The following outputs will be available for you to download as a `.csv` 
- Download the csv table with all the countries analysed and the representative percentage
- Download the csv table with only one country analysed
In order to analyse the country of your choice, you can choose from the following table, scraped from [Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes)
All countries belong to the EU.
- Austria
- Belgium
- Bulgaria
- Croatia
- Cyprus
- Czechia
- Denmark
- Estonia
- Finland
- France
- Germany
- Greece
- Hungary
- Ireland
- Italy
- Latvia
- Lithuania
- Luxembourg
- Malta
- Netherlands
- Poland
- Portugal
- Romania
- Slovakia
- Slovenia
- Spain
- Sweden
- United Kingdom

###Country analysis: Selected country
Depending on the country we analyze, the type of work and lifestyle of people. You can filter by country only or view global data.
You can see the data on the screen or download a csv. 

