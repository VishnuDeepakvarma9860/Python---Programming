from selenium import webdriver

# Modern Selenium automatically handles driver paths
driver = webdriver.Chrome() 
driver.get("https://www.google.com")
print(driver.title)
driver.quit()