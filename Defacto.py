import creds as creds
from bs4 import BeautifulSoup
import urllib.request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import pprint

#WE PROVIDE CHROME TO BE OPENED. THIS PART FOR CALCULATING PRODUCT OPTION AND ITS PROCESS.

# options = webdriver.ChromeOptions()
# browser = webdriver.Chrome(chrome_options=options)
# browser.get('https://www.defacto.com.tr/yeni-gelen-urunler')
# time.sleep(5)

#WE PROVIDE THE BUTTON TO SHOW ALL SIZES BY CREATING A BOT 

# product_count = len(browser.find_elements_by_xpath('//*[@class="picture"]/div/div/div/div/button'))
# 
# product_option_array = {}
# for i in range(3):
#     time.sleep(7)
#     python_button = browser.find_elements_by_xpath('//*[@class="picture"]/div/div/div/div/button')[i]
#
#     actions = ActionChains(browser)
#     actions.move_to_element(python_button)
#     # perform the operation on the element
#     actions.click(python_button).perform()
#
#     source_code = python_button.get_attribute("outerHTML")
#     print(source_code)
#
# for y in range(3):
#     time.sleep(5)
#     a_tags_count = browser.find_elements_by_xpath('//*[@class="btn-group"]/div/div/a')[y]
#     print(a_tags_count)

#
# for i in range(20):
#     a_tags_count = len(browser.find_elements_by_xpath('//*[@class="btn-group"]/div/div/a'))[0]
#     disabled_product=0
#     for y in range(a_tags_count):
#         time.sleep(5)
#         a_tags = browser.find_elements_by_xpath('//*[@class="btn-group"]/div/div/a')[y]
#         source_code = a_tags.get_attribute("outerHTML")
#         if len(source_code) > 1:
#             disabled_product += 1
#     if disabled_product != 0:
#         product_option_array[i] = (disabled_product / a_tags_count)
#     else:
#         product_option_array[i] = 0
#
#
# for k, v in product_option_array.items():
#     print("Product : {0}, Value : {1}".format(k, v))



# BS = BeautifulSoup(str(source_code),'html.parser')
# print(BS.a.attrs['class'])





#We provide the connection with google api
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('analytica.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Defacto').sheet1

#We are reading the yeni gelen ürünler's html document
url = "https://www.defacto.com.tr/yeni-gelen-urunler"
url_oku = urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku, "html.parser")


print("/*********************           YENİ GELEN ÜRÜNLER                     **************************")
print("/*************************************************************************************************")

urun = soup.find_all('div', attrs={'class': 'picture'})#Needed information is under picture attribute like price,url,sku
products = soup.find_all('div', attrs={'class': 'products-card'})





index=0
for i in range(len(urun)):
    urun_kodu = (urun[i].contents[1])

    index = i+2
    BS = BeautifulSoup(str(urun_kodu),'html.parser')
    pp = pprint.PrettyPrinter()
    sheet.update_cell(index, 1, BS.a.attrs['data-id'])
    sheet.update_cell(index, 2, BS.a.attrs['href'])
    sheet.update_cell(index, 3, BS.a.attrs['data-sale-price'])
    print(BS.a.attrs['data-id'])
    print(BS.a.attrs['href'])
    print(BS.a.attrs['data-sale-price'])

print("Siteden çekilen yeni gelen ürünlerin sayısı=")
print(len(urun))


print("/*********************                       KADIN                   *****************************")
print("/*************************************************************************************************")

#We are reading Kadın's html document
url2 = "https://www.defacto.com.tr/kadin"
url_oku2 = urllib.request.urlopen(url2)
soup2 = BeautifulSoup(url_oku2, "html.parser")



urun2 = soup2.find_all('div', attrs={'class': 'picture'})#Needed information is under picture attribute like price,url,sku

for j in range(len(urun2)):
            urun_kodu2 = (urun2[j].contents[1])
            index = index + 1

            BS2 = BeautifulSoup(str(urun_kodu2),'html.parser')
            pp2 = pprint.PrettyPrinter()
            sheet.update_cell(index, 1, BS2.a.attrs['data-id'])
            sheet.update_cell(index, 2, BS2.a.attrs['href'])
            sheet.update_cell(index, 3, BS2.a.attrs['data-sale-price'])

            print(BS2.a.attrs['data-id'])
            print(BS2.a.attrs['href'])
            print(BS2.a.attrs['data-sale-price'])

print("Siteden çekilen kadın ürünleri sayısı= ")
print(len(urun2))


print("/*********************                    ERKEK                      *****************************")
print("/*************************************************************************************************")

#We are reading Erkek's html document
url3 = "https://www.defacto.com.tr/erkek"
url_oku3 = urllib.request.urlopen(url3)
soup3 = BeautifulSoup(url_oku3, "html.parser")



urun3 = soup3.find_all('div', attrs={'class': 'picture'})#Needed information is under picture attribute like price,url,sku


for k in range(len(urun3)):
            urun_kodu3 = (urun3[k].contents[1])
            index = index + 1

            BS3 = BeautifulSoup(str(urun_kodu3),'html.parser')
            pp3 = pprint.PrettyPrinter()
            sheet.update_cell(index, 1, BS3.a.attrs['data-id'])
            sheet.update_cell(index, 2, BS3.a.attrs['href'])
            sheet.update_cell(index, 3, BS3.a.attrs['data-sale-price'])

            print(BS3.a.attrs['data-id'])
            print(BS3.a.attrs['href'])
            print(BS3.a.attrs['data-sale-price'])

print("Siteden çekilen erkek ürünleri sayısı= ")
print(len(urun3))

print("/*********************                 ÇOCUK & GENÇ               ********************************")
print("/*************************************************************************************************")

#We are reading Çocuk & Genç's html document
url4 = "https://www.defacto.com.tr/cocuk"
url_oku4 = urllib.request.urlopen(url4)
soup4 = BeautifulSoup(url_oku4, "html.parser")



urun4 = soup4.find_all('div', attrs={'class': 'picture'})#Needed information is under picture attribute like price,url,sku


for z in range(len(urun4)):
            urun_kodu4 = (urun4[z].contents[1])

            index = index + 1

            BS4 = BeautifulSoup(str(urun_kodu4),'html.parser')
            pp4 = pprint.PrettyPrinter()
            sheet.update_cell(index, 1, BS4.a.attrs['data-id'])
            sheet.update_cell(index, 2, BS4.a.attrs['href'])
            sheet.update_cell(index, 3, BS4.a.attrs['data-sale-price'])

            print(BS4.a.attrs['data-id'])
            print(BS4.a.attrs['href'])
            print(BS4.a.attrs['data-sale-price'])
print("Siteden çekilen çocuk ve genç ürünleri sayısı= ")
print(len(urun4))


print("/*********************                 BEBEK                    **********************************")
print("/*************************************************************************************************")

#We are reading Bebek's html document
url5 = "https://www.defacto.com.tr/bebek-giyim"
url_oku5 = urllib.request.urlopen(url5)
soup5 = BeautifulSoup(url_oku5, "html.parser")



urun5 = soup5.find_all('div', attrs={'class': 'picture'})#Needed information is under picture attribute like price,url,sku


for t in range(len(urun5)):
            urun_kodu5 = (urun5[t].contents[1])

            index = index + 1

            BS5 = BeautifulSoup(str(urun_kodu5),'html.parser')
            pp5 = pprint.PrettyPrinter()
            sheet.update_cell(index, 1, BS5.a.attrs['data-id'])
            sheet.update_cell(index, 2, BS5.a.attrs['href'])
            sheet.update_cell(index, 3, BS5.a.attrs['data-sale-price'])

            print(BS5.a.attrs['data-id'])
            print(BS5.a.attrs['href'])
            print(BS5.a.attrs['data-sale-price'])
print("Siteden Bebek ürünleri sayısı= ")
print(len(urun5))



print("/*********************                 AYAKKABI                    *******************************")
print("/*************************************************************************************************")

#We are reading Ayakkabı's html document
url6 = "https://www.defacto.com.tr/ayakkabi-modelleri"
url_oku6 = urllib.request.urlopen(url6)
soup6 = BeautifulSoup(url_oku6, "html.parser")



urun6 = soup6.find_all('div', attrs={'class': 'picture'})#Needed information is under picture attribute like price,url,sku


for v in range(len(urun6)):
            urun_kodu6 = (urun6[v].contents[1])
            index = index + 1

            BS6 = BeautifulSoup(str(urun_kodu6),'html.parser')
            pp6 = pprint.PrettyPrinter()
            sheet.update_cell(index, 1, BS6.a.attrs['data-id'])
            sheet.update_cell(index, 2, BS6.a.attrs['href'])
            sheet.update_cell(index, 3, BS6.a.attrs['data-sale-price'])

            print(BS6.a.attrs['data-id'])
            print(BS6.a.attrs['href'])
            print(BS6.a.attrs['data-sale-price'])

print("Siteden çekilen ayakkabı sayısı= ")
print(len(urun6))


print("/*********************                 AKSESUAR                    *******************************")
print("/*************************************************************************************************")

#We are reading Aksesuar's html document
url7 = "https://www.defacto.com.tr/aksesuar"
url_oku7 = urllib.request.urlopen(url7)
soup7 = BeautifulSoup(url_oku7, "html.parser")



urun7 = soup7.find_all('div', attrs={'class': 'picture'})#Needed information is under picture attribute like price,url,sku

for u in range(len(urun7)):
            urun_kodu7 = (urun7[u].contents[1])

            index = index + 1

            BS7 = BeautifulSoup(str(urun_kodu7),'html.parser')
            pp7 = pprint.PrettyPrinter()
            sheet.update_cell(index, 1, BS7.a.attrs['data-id'])
            sheet.update_cell(index, 2, BS7.a.attrs['href'])
            sheet.update_cell(index, 3, BS7.a.attrs['data-sale-price'])

            print(BS7.a.attrs['data-id'])
            print(BS7.a.attrs['href'])
            print(BS7.a.attrs['data-sale-price'])

print("Siteden çekilen aksesuar sayısı= ")
print(len(urun7))
