


import os
os.getcwd()


from selenium import webdriver


driver = webdriver.Chrome(executable_path = '/Users/megangillen/Documents/megans-project/chromedriver')

driver.get('http://www.google.com')

# create a new Chrome session driver = webdriver.Chrome(executable_path='../chromedriver')
  # Navigate to the application home page driver.get("http://www.google.com")


searchbox = driver.find_element_by_name('q')
searchbox.send_keys('puppies')
searchbox.submit()
driver.find_element_by_class_name('st').text


driver.get('http://www.vsco.com')
signin = driver.find_element_by_class_name('Nav-text')
signin.su
