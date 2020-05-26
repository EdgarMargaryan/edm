# Simple assignment


from selenium.webdriver import Chrome

from selenium.webdriver.common.keys import Keys

driver = Chrome()
with Chrome() as driver:
    driver.get("http://the-internet.herokuapp.com/login")
    driver.maximize_window()
    url = driver.current_url
    print(url)
    title = driver.title
    print(title)
    assert (url == "http://the-internet.herokuapp.com/login")
    assert (title == "The Internet")

    LogIn_Field = driver.find_element_by_id("username")
    LogIn_Field.send_keys("UserTest")
    Password_Field = driver.find_element_by_id("password")
    Password_Field.send_keys("UserPassword" + Keys.ENTER)

    driver.quit()
