from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "C:/Users/Hello/Chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event_dict = [(n, {"time": event_times[n].text, "name": event_names[n].text}) for n in range(len(event_times))]

# for n in range(len(event_times)):
#     dict_item = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
#     event_dict[n] = dict_item
print(event_dict)

driver.close()
#driver.quit()