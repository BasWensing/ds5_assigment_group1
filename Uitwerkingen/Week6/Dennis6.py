# Opdracht 2
import pandas as pd
import matplotlib.pyplot as plt

""" Functie definiëren". Dennis"""
def generate_sales_report (file_path):

    """ Bestand inlezen vanuit Excel. Dennis"""
    df = pd.read_excel(file_path)

    """ Berekeningen uitvoeren. Dennis """

    """ Functie hiervoor aanmaken. Dennis"""
    def berekeningen(file_path):
        category_sales =  df.groupby('Category')['Sales'].sum()
        total_sales = category_sales.sum()
        percentage_of_sales = category_sales / total_sales * 100
        sales_per_month = df.groupby('Month')['Sales'].sum()
        percentage_month_contribution = sales_per_month / total_sales * 100
        return category_sales, percentage_of_sales, sales_per_month, percentage_month_contribution

    """ Berekeningen uitvoeren. Dennis"""
    [category_sales, percentage_of_sales, sales_per_month, percentage_month_contribution] = berekeningen(file_path)

    print(category_sales)
    print(sales_per_month)


    """ Dataframe aanmaken voor berekeningen per categorie. Dennis"""
    report_categories = pd.DataFrame({'Sales per category': category_sales,
                                      'Percentage that category contributes to total sales': percentage_of_sales})
    
    """ Dataframe aanmaken voor berekeningen per maand. Dennis"""
    report_months = pd.DataFrame({'Sales per month': sales_per_month,
                                  'Percentage of total sales': percentage_month_contribution})

    """ Twee dataframes bij elkaar voegen tot één dataframe. Dennis"""
    report = pd.concat([report_categories.reset_index(), report_months.reset_index()], axis=1)

    """ Raport teruggeven. Dennis"""
    return report

""" Functie uitvoeren, raport genereren. Dennis"""
report = generate_sales_report('retail.xlsx')
print(report)

""" Rapport exporteren naar Excel. Dennis"""
report.to_excel('reportRetail.xlsx')

