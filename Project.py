from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client

#Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a formatted output one currency at a time. 
# The output should display the name of the currency, the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)
#Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.
#Submit your GitHub URL which should contain all the files worked in class as well as the above.

##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"

url = 'https://crypto.com/price/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

names = soup.findAll("span", attrs={"class":"chakra-text css-1mrk1dy"})
symbols = soup.findAll("span",attrs={"class":"chakra-text css-ft1qn5"})
prices = soup.findAll("div",attrs={"class":"css-b1ilzc"})

counter = 0
number_to_display = 5
while counter < number_to_display:
    #Name
    for name in names[counter:(counter+1)]:
        current_name = name.text.strip()

    #Symbol
    for symbol in symbols[counter:(counter+1)]:
        current_symbol = symbol.text.strip()

    #Price
    for price in prices[counter:(counter+1)]:
        current_price = float(price.text.strip().replace(',','').replace('$',''))

    #% Change
    rows = soup.findAll('tr')
    for row in rows[counter+1:number_to_display+1]:
        td = row.findAll('td')
        current_percent = td[4].text.strip()
        calc_percent = (float(td[4].text.strip().replace('%','').replace('+',''))/100)
        break
    
    change = (-1*(calc_percent)) * current_price

    previous = current_price + change

    #Output   
    print("Name: " + current_name)
    print("Symbol: " + current_symbol)
    print("Price: " + str(current_price))
    print("24H Change: " + str(current_percent))
    print("Previous Price: " + str(previous))
    input()

    #Counter
    counter+=1 

#Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.

    ETH_notif = False
    BTC_notif = False
    if current_symbol == "BTC" or "ETH":
        if current_symbol == "BTC":
            if current_price < 40000:
                BTC_notif = True
        elif symbol == 'ETH':
            if price < 3000:
                ETH_notif = True

accountSID = "AC2d3aa0f6d18dfe8d06730f99c0538265"
authToken = "d821ed08d06959b46bdba18b39f55b4c"
client = Client(accountSID,authToken)
TwilioNumber = "+16098045645"
mycellphone = "+13464209748"

if ETH_notif == True:
    textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body="ETH has dropped below 3000! BUY BUY BUY")
    print(textmessage.status)
if BTC_notif == True:
    textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body="BTC has dropped below 40,000! BUY BUY BUY")
    print(textmessage.status)
