from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

#Chrome

driver=webdriver.Chrome(executable_path=r"C:\Users\Aram\Desktop\chromedriver")
#driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.python.org/")
driver.maximize_window()
search=driver.find_element_by_id("id-search-field").send_keys("bla bla")
go=driver.find_element_by_id("submit").click()
time.sleep(3)
x=driver.find_element_by_xpath("/html/body/div/div[3]/div/section/form/ul/p").text
print(x)
print(driver.current_url)
print(driver.title)
driver.close()                                                                                                                                                                  
print("Your session is successfully done!")

#Firefox

driver=webdriver.Firefox(executable_path=r"C:\Users\Aram\Desktop\geckodriver")
#driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.python.org/")
driver.maximize_window()
search=driver.find_element_by_id("id-search-field").send_keys("bla bla")
go=driver.find_element_by_id("submit").click()
time.sleep(3)
x=driver.find_element_by_xpath("/html/body/div/div[3]/div/section/form/ul/p").text
print(x)
print(driver.current_url)
print(driver.title)
driver.close()                                                                                                                                                                  
print("Your session is successfully done!")
