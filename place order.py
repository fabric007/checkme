import requests                                        
import time 
import win32gui, win32con
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select


#from selenium.webdriver.common.keys import Keys


from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

url = "https://nishita.waverfid.group/#/"
driver.get(url)
time.sleep(5)
               
driver.find_element_by_name('email').send_keys('nishitaporiya@atyantik.com')
driver.find_element_by_name('password').send_keys('atyantik@123')

button = driver.find_element_by_css_selector('.input-group .btn')
button.click()

url = "https://nishita.waverfid.group/#/dashboard"
time.sleep(5)
if (driver.current_url == url):
    print ("login Test case passed")
else: 
    print("login is failed")
    time.sleep(5)
    
 #click on frame module      
driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div/ul/li[1]/a").click()
time.sleep(4)
print("click on frame option")

#click on search         
driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div[12]/section/div/div/a").click()
time.sleep(4)
print("click on search")

 #search by mfg
driver.find_element_by_name('manufacturer').send_keys('fastrack')
time.sleep(2)

#click on search button for results        
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[12]/section/div/div/form/div/div[1]/button[1]").click()
time.sleep(4)
print("click on search button for results")

driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/div").click()
time.sleep(4)
print("1st frame of fastrack ")

driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/div").click()
time.sleep(8)
print("2nd frame of fastrack")

driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/div[2]/div[4]/div[2]/button").click()
time.sleep(4)
print("click on review order")


#add quantity:12
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[1]/td[4]/table/tbody/tr[1]/td[3]/input").clear( )
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[1]/td[4]/table/tbody/tr[1]/td[3]/input").send_keys('12')
time.sleep(4)
print("add quantity:12")


#add cost 
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[1]/td[4]/table/tbody/tr[1]/td[4]/input").clear( )
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[1]/td[4]/table/tbody/tr[1]/td[4]/input").send_keys('100.9900')
print("add cost:100.9900")

#add quantity:10
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[3]/input").clear( )
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[3]/input").send_keys('10')
time.sleep(4)
print("add quantity:12")


#add cost 
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[4]/input").clear( )
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[2]/td[4]/table/tbody/tr[1]/td[4]/input").send_keys('100.9900')
print("add cost:100.9900")


#select location 
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/div/div[1]/select").click()
time.sleep(2)   
obj=Select (driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/div/div[1]/select"))
obj.select_by_value("1")
print("select location:1")


#display the selected location.
time.sleep(2)
text=driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[1]/div/div[1]/select").text
print(text)

#select confirm button
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[4]/td/div/input[1]").click()
time.sleep(2)

if driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[4]/td/div/input[1]").text:
    print("test case is pass")
    round(2221.78,2)              
else:
    print("Test Failed")
    #return false
    
#Confirm Order
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[3]/div/div/div/form/div/table/tbody/tr[4]/td/div/input[1]").click()
time.sleep(5) 
print("confirm order")