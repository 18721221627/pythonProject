from time import sleep
from selenium import webdriver


driver = webdriver.Remote(
command_executor='http://10.242.130.113:5555/wd/hub',
desired_capabilities={'browserName': 'firefox'}
)

driver.get('https://www.baidu.com')
print("start run")

driver.find_element_by_id("kw").send_keys("docker selenium")
driver.find_element_by_id("su").click()
driver.save_screenshot('login1.png')

sleep(1)

driver.quit()
print("end...")