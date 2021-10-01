from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://poshanabhiyaan.gov.in/#/login")
username = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
username.send_keys("mow&cd-2750011")
password = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
password.send_keys("Nandura@123")
time.sleep(60)

total = driver.find_element_by_xpath('//*[contains (@placeholder, "Number")]')
adultmale = driver.find_element_by_xpath('//*[@id="id1"]/th[2]/input')
adultfemale = driver.find_element_by_xpath('//*[@id="id1"]/th[3]/input')
childmale = driver.find_element_by_xpath('//*[@id="id2"]/th[2]/input')
childfemale = driver.find_element_by_xpath('//*[@id="id2"]/th[3]/input')
Description = driver.find_element_by_xpath('//*[@id="mat-input-5"]')
select = driver.find_element_by_xpath('//button[contains(text(),"SUBMIT")]')
# activity = driver.find_element_by_xpath('//button[contains(text(),"Add another activity")]')
town = ["Shamba 1","Shamba 2","Shamba 3","Wadi 1","Wadi 2","Wadi 3","Digi 1","Digi 2","Digi 3","Kati 1","Kati 2","Wasadi Bdk 1","Wasadi Bdk 2","Wasadi khu","Lonwadi 1", "Lonwadi 2","Pimpalkhuta 1","Pimpalkuta 2","Shalgaon 1","Shalgaon 2","Shalgaon 3","Potali 1","Potali 2","Potali 3","Naigaon 1","Naigaon 2","Tekodi","Walti Bhu","Walti Khu","Khandale","Fuli 1","Fuli 2","Goshing","Khadgaon 1","Khdgaon 2","Tandulwadi","Shamba Khu","Kurshinagar","Wadner 1","Wadner 2","Wadner 3","Wadner 4","Wadner 5","Wadner 6","Wadner 7","Wadner 8","Wadner 9","Wadner 10","Wadner 11","Wadner 12","Sirsodi 1","Sirsodi 2","Kokalwadi","Bhurti","Vatali","Sanpudi","Aurampur",]
# town = []
# town = ["Shamba 1","Shamba 2","Shamba 3", "Wasadi Bdk 1","Wasadi Bdk 2","Wasadi khu","Lonwadi 1","Lonwadi 2","Pimpalkhuta 1","Pimpalkuta 2","Shalgaon 1","Shalgaon 2","Shalgaon 3","Potali 1","Potali 2","Potali 3","Naigaon 1","Naigaon 2","Tekodi","Walti Bhu","Walti Khu","Khandale","Fuli 1","Fuli 2","Goshing","Khadgaon 1","Khdgaon 2","Tandulwadi","Shamba Khu","Kurshinagar"]
x= len(town)

# time.sleep(1)
# total.send_keys('21')
# adultmale.send_keys('4')
# adultfemale.send_keys('5')
# childmale.send_keys('5')
# childfemale.send_keys('7')
# Description.send_keys(town[1])
# select.click()
# WebDriverWait(driver, 60).until(EC.alert_is_present())
# driver.switch_to.alert.accept()
# time.sleep(13

# for k in  range(6):
for i in range(x):
    for j in range(11):
        if j==1 or j==9:
            # time.sleep(0)
            total.send_keys('22')
            adultmale.send_keys('4')
            adultfemale.send_keys('5')
            childmale.send_keys('6')
            childfemale.send_keys('7')
            Description.send_keys(town[i])
            select.click()
            # WebDriverWait(driver, 10).until(EC.alert_is_present())
            # driver.switch_to.alert.accept()
            time.sleep(2)
        elif j==2 or j==10:
            # time.sleep(0)
            total.send_keys('22')
            adultmale.send_keys('5')
            adultfemale.send_keys('4')
            childmale.send_keys('6')
            childfemale.send_keys('7')
            Description.send_keys(town[i])
            select.click()
            # WebDriverWait(driver, 10).until(EC.alert_is_present())
            # driver.switch_to.alert.accept()
            time.sleep(2)
            
        elif j==3 or j==8:
            # time.sleep(0)
            total.send_keys('17')
            adultmale.send_keys('3')
            adultfemale.send_keys('3')
            childmale.send_keys('5')
            childfemale.send_keys('6')
            Description.send_keys(town[i])
            select.click()
            # WebDriverWait(driver, 10).until(EC.alert_is_present())
            # driver.switch_to.alert.accept()
            time.sleep(2)
            
            
            
            

        elif j==4 or j==6:
            # time.sleep(0)
            total.send_keys('20')
            adultmale.send_keys('3')
            adultfemale.send_keys('4')
            childmale.send_keys('6')
            childfemale.send_keys('7')
            Description.send_keys(town[i])
            select.click()
            # WebDriverWait(driver, 10).until(EC.alert_is_present())
            # driver.switch_to.alert.accept()
            time.sleep(2)
            
            
            
            
            
        elif j==5 or j==7:
            # time.sleep(0)
            total.send_keys('20')
            adultmale.send_keys('4')
            adultfemale.send_keys('4')
            childmale.send_keys('5')
            childfemale.send_keys('7')
            Description.send_keys(town[i])
            select.click()
            # WebDriverWait(driver, 10).until(EC.alert_is_present())
            # driver.switch_to.alert.accept()
            time.sleep(2)
            