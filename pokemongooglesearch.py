from time import sleep
import re
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

search_words = []

#CSVファイルからポケモン日本語名データの読込
f = open("pokemon_name.csv", "r", encoding="utf-8")
reader = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
for row in reader:
   search_words.append(row[0])
#print(search_words)
f.close()


#CSVファイルの作成
csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = 'pokemon_google_search_' + csv_date + '.csv'
f = open(csv_file_name, 'w', encoding='utf-8', errors='ignore')
writer = csv.writer(f, lineterminator='\n')

options = Options()
options.add_argument('--headless') ##

driver = webdriver.Chrome(executable_path="/Applications/chromedriver", options=options)
index = 1

for search_word in search_words:
    url = "https://www.google.com/search?q="
    url += search_word
    driver.get(url)
    sleep(5)
    
    element = driver.find_element_by_id("result-stats")
    number_result = int(element.text.replace(",", "").split()[1])

    csvlist = []
    csvlist.append(str(index))
    csvlist.append(search_word)
    csvlist.append(number_result)
    writer.writerow(csvlist)

    print(csvlist)
    index += 1

f.close()
driver.close()