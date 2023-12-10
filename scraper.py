import requests
from bs4 import BeautifulSoup

l=list()
obj={}

# URL of the Zillow page you want to scrape
target_url = 'https://www.zillow.com/il/sold/'

# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

# resp =  requests.get(target_url, headers=headers)

# print(resp.status_code)

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
         "Accept-Language":"en-US,en;q=0.9",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
         "Accept-Encoding":"gzip, deflate, br",
         "upgrade-insecure-requests":"1"}

resp = requests.get(target_url, headers=headers).text

soup = BeautifulSoup(resp,'html.parser')

properties = soup.find_all("div",{"class":"StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0 bKpguY property-card-data"})

for x in range(0,len(properties)):
    try:
        obj['pricing']=properties[x].find("div",{"class":"StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 fDSTNn"}).text
    except:
        obj["pricing"]=None

    try:
        obj['size']=properties[x].find("div",{"class":"StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 dbDWjx"}).text
    except:
        obj["size"]=None

    l.append(obj)
    obj={}
print(l)


# <div class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 dbDWjx"><ul class="StyledPropertyCardHomeDetailsList-c11n-8-84-3__sc-1xvdaej-0 eYPFID"><li><b>--</b> <abbr>bds</abbr></li><li><b>--</b> <abbr>ba</abbr></li><li><b>--</b> <abbr>sqft</abbr></li></ul> - Sold</div>

# <div class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 fDSTNn"><div class="PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 kSsByo"><span data-test="property-card-price" class="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr">$138,000</span></div></div>
# <div class="StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0 bKpguY property-card-data"><a href="https://www.zillow.com/homedetails/2415-College-Dr-Mount-Carmel-IL-62863/115753757_zpid/" data-test="property-card-link" class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link" tabindex="0"><address data-test="property-card-addr">2415 College Dr, Mount Carmel, IL 62863</address></a><div class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jretvB"></div><div class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 fDSTNn"><div class="PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 kSsByo"><span data-test="property-card-price" class="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr">$138,000</span></div></div><div class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 dbDWjx"><ul class="StyledPropertyCardHomeDetailsList-c11n-8-84-3__sc-1xvdaej-0 eYPFID"><li><b>--</b> <abbr>bds</abbr></li><li><b>--</b> <abbr>ba</abbr></li><li><b>--</b> <abbr>sqft</abbr></li></ul> - Sold</div></div>

# <div class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 fDSTNn">
#     <div class="PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 kSsByo">
#         <span data-test="property-card-price" class="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr">$138,000</span>
#     </div>
# </div>