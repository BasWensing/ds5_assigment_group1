# Opdracht 2
import pandas as pd
import matplotlib.pyplot as plt

def clean_data_and_generate_report(file_path):

    def data_cleaning(file_path):
        df = pd.read_excel(file_path)

        """ Unieke waarden bekijken voor alle kolommen. Dennis"""
        unique_values_category = (df['Category'].unique())
        unique_values_month = (df['Month'].unique())
        unique_values_sales = (df['Sales'].unique())

        df.loc[df['Month'] == 'Feburary', 'Month'] = 'February' # Maand 'feburary' correct omzetten in 'February'

        """ Dataframe retourneren. Dennis"""
        return df

    """ Data-cleaning uitvoeren. Dennis"""
    file_path = data_cleaning('retail.xlsx')

    """ Dataframe exporteren naar Excel. Dennis"""
    file_path.to_excel('retail_cleaned.xlsx') # Dataframe exporteren naar exc

    """ Functie definiëren". Dennis"""
    def generate_sales_report (file_path):

        """ Bestand inlezen vanuit Excel. Dennis"""
        df = pd.read_excel(file_path)

        """ Functie voor berekeningen aanmaken. Dennis"""
        def berekeningen(file_path):
            category_sales =  df.groupby('Category')['Sales'].sum() # Sales per category berekenen
            total_sales = category_sales.sum() # Totaal aantal sales berekenen
            percentage_of_sales = category_sales / total_sales * 100 # Percentage sales per categorie berekenen
            sales_per_month = df.groupby('Month')['Sales'].sum() # Aantal sales per maand berekenen
            percentage_month_contribution = sales_per_month / total_sales * 100 # Percentage sales per maand berekenen
            return category_sales, percentage_of_sales, sales_per_month, percentage_month_contribution

        """ Berekeningen uitvoeren. Dennis"""
        [category_sales, percentage_of_sales, sales_per_month, percentage_month_contribution] = berekeningen(file_path)


        """ Dataframe aanmaken voor berekeningen per categorie. Dennis"""
        def rapport_maken (kolom1, kolom2, kolom3, kolom4):
            report_categories = pd.DataFrame({'Sales per category': category_sales, # Dataframe aanmaken voor berekeningen categorieën
                                            'Percentage that category contributes to total sales (%)': percentage_of_sales})
            
            """ Dataframe aanmaken voor berekeningen per maand. Dennis"""
            report_months = pd.DataFrame({'Sales per month': sales_per_month, # Dataframe aanmaken voor berekeningen maanden
                                        'Percentage of total sales (%)': percentage_month_contribution})

            """ Twee dataframes bij elkaar voegen tot één dataframe. Dennis"""
            dataframe_report = pd.concat([report_categories.reset_index(), report_months.reset_index()], axis=1)

            """ Samengesteld rapport teruggeven. Dennis"""
            return dataframe_report

        dataframe_report = rapport_maken (category_sales, percentage_of_sales, sales_per_month, percentage_month_contribution)

        """ Rapport teruggeven. Dennis"""
        return dataframe_report

    report = generate_sales_report ('retail_cleaned.xlsx')
    return report

""" Functie uitvoeren, rapport genereren. Dennis"""
report = clean_data_and_generate_report('retail.xlsx')
print(report) # Rapport uitpinten

""" Rapport exporteren naar Excel. Dennis"""
report.to_excel('reportRetail.xlsx')
