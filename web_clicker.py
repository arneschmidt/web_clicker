from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
while True:
    try:

        driver.get("https://cqm.cleverq.de/public/appointments/lk_hameln_pyrmont_kfz/index.html?lang=de")
        time.sleep(0.5)
        driver.find_elements_by_xpath('//*[@id="background-image"]/div[2]/div[2]/div[2]/div[2]/div[2]/button')[0].click()
        time.sleep(0.5)
        driver.find_elements_by_xpath('//*[@id="background-image"]/div[2]/div[3]/div[2]/div[2]/div[4]/button[1]')[0].click()
        time.sleep(0.5)
        driver.find_elements_by_xpath('//*[@id="background-image"]/div[2]/div[5]/div/div/div/button')[0].click()
        time.sleep(2)
        text=driver.find_element_by_class_name("tab-content").text
        termine = [int(s) for s in text.split() if s.isdigit()]
        for termin in termine:
            if termin ==10:
                print("########################")
                print(termine)
                time.sleep(10)
            else:
                os.system('clear')
        print(text)
    except:
        print("Problem, I try again")
        time.sleep(2)
driver.close()
