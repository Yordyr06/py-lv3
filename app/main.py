import utils
import csv_reader
import charts
import pandas as pd

def run():
  data = csv_reader.read_csv('data.csv')
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'South America']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  country = input('Enter a country =>  ')
  result = utils.population_by_country(data, country)

  if len(result) > 0: 
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()