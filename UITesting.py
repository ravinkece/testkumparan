import HTMLTestRunner
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Python34\chromedriver.exe')
driver.get("http://www.kumparan.com")
time.sleep(3)
popup = driver.find_element_by_id ("onesignal-popover-dialog")
if assert "Nyalakan notifikasi untuk mendapatkan update berita terkini dari kumparan" in popup.text :
	print "Verified"
else:
	print "Nothing"
berita = driver.find_element_by_xpath("//*[@id=\"content\"]/div/div/div/div[2]/div/div[5]/a[1]/label/div/div/div/div/span")
assert "News" in berita