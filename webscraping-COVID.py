# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll("tr")

highest_death_ratio_state = ""
highest_death_ratio = 0

highest_testing_ratio_state = ""
highest_testing_ratio = 0

lowest_testing_ratio_state = ""
lowest_testing_ratio = 100

for row in table_rows[2:51]:
    td = row.findAll("td")
    state_rank = td[0].text.strip()
    state_name = td[1].text
    total_cases = int(td[2].text.replace(",",""))
    #new_cases = int(td[3].text.replace(",",""))
    total_deaths = int(td[4].text.replace(",",""))
    #new_deaths = int(td[5].text.replace(",",""))
    #total_recovered = int(td[6].text.replace(",",""))
    #active_cases = int(td[7].text.replace(",",""))
    tot_cases_1m_pop = int(td[8].text.replace(",",""))
    deaths_1m_pop = int(td[9].text.replace(",",""))
    total_tested = int(td[10].text.replace(",",""))
    tests_1m_pop = int(td[11].text.replace(",",""))
    population = int(td[12].text.replace(",",""))

    #highest death ratio (deaths/cases), highest testing ratio (total tested/total cases) and lowest testing ratio
    #print("-"*20)
    #print(f"STATE NAME = {state_name}")
    #print(f"Total Cases = {total_cases}")
    #print(f"Total Deaths = {total_deaths}")
    #print(f"Total Tested = {total_tested}")
    #print("-"*20)

    death_ratio = total_deaths/total_cases
    test_ratio = total_cases/total_tested

    if death_ratio > highest_death_ratio:
        highest_death_ratio = death_ratio
        highest_death_ratio_state = state_name
    
    if test_ratio > highest_testing_ratio:
        highest_testing_ratio = test_ratio
        highest_testing_ratio_state = state_name
    
    if test_ratio < lowest_testing_ratio:
        lowest_testing_ratio = test_ratio
        lowest_testing_ratio_state = state_name

print(highest_death_ratio_state)
print(highest_death_ratio)

print(highest_testing_ratio_state)
print(highest_testing_ratio)

print(lowest_testing_ratio_state)
print(lowest_testing_ratio)

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

