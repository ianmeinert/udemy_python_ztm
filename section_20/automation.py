from selenium import webdriver
from selenium.webdriver.common.by import By
import time

edge_browser = webdriver.Edge()
edge_browser.maximize_window()
edge_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

user_message = edge_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

time.sleep(2)
show_message_button = edge_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()

output_message = edge_browser.find_element(By.ID, 'display')

edge_browser.close()
