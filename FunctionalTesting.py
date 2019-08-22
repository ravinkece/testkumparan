#browser.execute_script("window.scrollTo(0,500)")
import HTMLTestRunner
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Python34\chromedriver.exe')
driver.get("http://www.kumparan.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"content\"]/div/div/div/div[2]/div/div[5]/a[1]/label/div/div/div/div/span").click()
time.sleep(2)
driver.find_element_by_partial_link_text("//*[@id=\"content\"]/div/div/div/div[4]/div/div/div/div/div[1]/div[7]/div/div/div[2]/div/div[4]/div/div/div/div/div/div/div[1]/div[1]/div/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"content\"]/div/div/div/div[4]/div/div/div[2]/div/div[1]/div[3]/div[4]/div/div/div/div[2]/div/div/div/div/div/div[1]").send_keys("Berita yang sangat bagus")
time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"track_submit_comment\"]/span/div/div/img")