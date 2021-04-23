from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.support.ui import Select  
#import time

def test_login(driver):
    driver.get("http://192.168.131.10/monitoring_3cardf_39/upc3cardf/login?type=U")

    assert "Управление процессинговым центром 3Card-F 3Card-F" in driver.title


    login_field = driver.find_elements_by_xpath("/html/body/form/center[2]/table/tbody/tr[2]/td[2]/input[1]")
    login_field[0].send_keys('spars')
    password_field = driver.find_element_by_xpath("/html/body/form/center[2]/table/tbody/tr[2]/td[2]/input[2]").send_keys('manager')
    click_enter = driver.find_element_by_id('sbm').click()
    driver.implicitly_wait(10)
    find_text = driver.find_element_by_class_name("license")


def stop_pc(driver):
    driver.implicitly_wait(10)
    stop_btn = driver.find_element_by_css_selector("#work_area > div.group_4 > div.stop")
    stop_btn.click()
    driver.implicitly_wait(10)
    find_text = driver.find_element_by_css_selector("#work_area > div:nth-child(4) > div.group_4 > p > em")
    print("Процессинговый центр 3CardF остановлен")


chrome_options = Options() 
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome(r'C:\\Driver\\chromedriver.exe', options=chrome_options)
test_login(driver)
stop_pc(driver)

driver.quit();
