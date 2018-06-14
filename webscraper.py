import os, time, csv
from selenium import webdriver  #launch a browser
from selenium.webdriver.common.by import By # search for specific parameters
from selenium.webdriver.support.ui import WebDriverWait # wait for a page to load
from selenium.webdriver.support import expected_conditions as EC # expected condition of how the page should be after it has loaded
from selenium.common.exceptions import TimeoutException # handling a timeout situation
from selenium.webdriver.common.keys import Keys # to input things in forms

def try_waiting(xpath):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        print("Timed out waiting for page to load.")
        browser.quit()

# if this doesn't work, export PATH=$PATH:/path/to/driver/exe
def main():
    browser = webdriver.Firefox()
    login_url = "https://www.picknsave.com/signin"

    browser.get(login_url)

    # timeout for website to load
    timeout = 20
    wait = WebDriverWait(browser, timeout)

    try_waiting("//img[@class='Image']")

    username_input = browser.find_element_by_id("SignIn-emailInput")
    password_input = browser.find_element_by_id("SignIn-passwordInput")

    # sleeping because I'm not sure if the site checks for bot activity or not?
    username_input.send_keys("username_goes_here") # redacted :)
    time.sleep(2)

    password_input.send_keys("password_goes_here") # redacted :)
    time.sleep(2)

    browser.find_element_by_id("SignIn-submitButton").click()
    time.sleep(3)

    try_waiting("//img[@class='Image']")
    browser.find_element_by_xpath("//div[@class='SignInWrapper']").click()

    try_waiting("//ul[@class='SignedInMenuList']")
    browser.find_element_by_xpath("//a[@href='https://www.picknsave.com/account/update']").click()

    try_waiting("//img[@class='Image']")
    browser.find_element_by_xpath("//a[@href='/mypurchases']").click()

    try_waiting("//div[@class='ReceiptList-listContent']")
    trips = browser.find_elements_by_class_name("ReceiptList-line")
    trips.pop(0)

    # scraping information about purchases
    for i in range(len(trips)):
        try_waiting("//img[@class='Image']")
        trips = browser.find_elements_by_class_name("ReceiptList-line") # refreshes the list
        trips.pop(0)

        try_waiting("//img[@class='Image']")
        trips[i].find_element_by_class_name("ReceiptList-receiptDateLink").click() # click on date of purchase

        purchases = browser.find_elements_by_xpath("//div[@role='row']")

        for j in range(len(purchases)):

            item_attributes = []

            purchases = browser.find_elements_by_xpath("//div[@role='row']")

            with open("grocery_data.csv", "w") as csvfile:
                fieldnames = ["Item Name", "Item Amount", "Unit Price", "Savings", "Price Paid"]
                writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

                item_attributes.append(purchases[j].find_element_by_xpath("./a[@class='ReceiptDetail-itemName']").get_attribute("innerHTML"))

                writer.writeheader()
                writer.writerow({"Item Name": item_attributes[0]})
                writer.writerow({"Item Amount": item_attributes[1]})
                writer.writerow({"Unit Price": item_attributes[2]})
                writer.writerow({"Savings": item_attributes[3]})
                writer.writerow({"Price Paid": item_attributes[4]})


        try_waiting("//button[@data-qa='rcpt_receipt_list']")
        browser.find_element_by_xpath("//button[@data-qa='rcpt_receipt_list']").click()

if __name__ == "__main__":
    main()
