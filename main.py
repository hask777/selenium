from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('C:/Users/Hask777/Downloads/chromedriver_win32/chromedriver')

# url = "http://the-internet.herokuapp.com/login"

# driver.get(url)

# driver.find_element_by_xpath('//*[@id="username"]').send_keys('tomsmith')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('SuperSecretPassword!')
# driver.find_element_by_xpath('//*[@id="login"]/button').click()

# driver.quit()


url = "http://the-internet.herokuapp.com/dynamic_loading/2"
driver.get(url)

driver.find_element_by_xpath('//*[@id="start"]/button').click()
driver.implicitly_wait(10)
text = driver.find_element_by_xpath('//*[@id="finish"]/h4').text

print(text)