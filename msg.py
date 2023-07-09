from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

# Set Chrome options 
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Instantiate ChromeDriver with options
driver = webdriver.Chrome(executable_path="chromedriver")

driver.get("https://web.whatsapp.com")
time.sleep(20)

def msg():
    name = input('\nEnter Group/User Name: ')
    message = input("Enter your message to group/user: ")
    Count = int(input("Enter the message count:"))

    # Find Whom to message     
    
    # user = driver.find_element("x_path",'//span[@title = "{}"]'.format(name))
    # user.click()
    user = driver.find_element(By.XPATH,'//span[@title = "{}"]'.format(name))
    user.click()

    text_box = driver.find_element(By.CLASS_NAME,'_3Uu1_')

    #Send Button
    for i in range(Count):
        text_box.send_keys(message + Keys.ENTER)
        # element = WebDriverWait(driver, 20).until(
        # EC.element_to_be_clickable((By.CSS_SELECTOR,".tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq")))
        # element.click() 
msg()


def reps():
    print("Do you want to send more msg to anyone")
    askUser = input("Press y for Yes and n for No : ")
    if (askUser == 'Y' or askUser == 'y'):
        msg()
        reps()
    elif (askUser == 'N' or askUser == 'n'):
        print("Thank you see you soon")
    else:
        print("Please Enter Valid option :\n")
        reps()
reps()

