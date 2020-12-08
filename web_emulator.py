from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome('A:\Dropbox (GaTech)\Programming\CIOS\Driver\chromedriver') # Create instance of browser
wait = WebDriverWait(driver, 10)

def login():
    email = "sregenbaum3@gatech.edu"
    username = "sregenbaum3"
    password = "j01vTR90eLPz"   

    driver.get("https://wwwh.smartevals.com/SchoolList.aspx?from=anonseeresults") # Go to smart Evals

    email_login = driver.find_element_by_name("_ctl0:cphContent:txtEmail")
    email_login.send_keys(email)
    email_login.send_keys(Keys.RETURN)

    gatech_login_username = driver.find_element_by_name("username")
    gatech_login_password = driver.find_element_by_name("password")
    gatech_login_username.send_keys(username)
    gatech_login_password.send_keys(password)
    gatech_login_password.send_keys(Keys.RETURN)

    return 1

def goToResults(status):
    if not status:
        return 0

    year = 2019
    form = 2021 - year

    wait.until(lambda driver: driver.find_elements_by_id("lnkSeeResultsImg"))

    button = driver.find_element_by_id("_ctl0_lnkSeeResults")
    button.click()

    option = driver.find_element_by_xpath("//*[@id='panYears']/a[" + str(form) + "]")
    option.send_keys("\n")
    return 1

def scrapeResults(status):
    if not status:
        return 0

    pages = 100
    z = 0
    
    for j in range(0, pages):
        wait.until(lambda driver: driver.find_elements_by_id("_ctl0_cphContent_grd1_DXPagerBottom"))

        option_num = 10

        if j < 1:
            try: #If 2020: 6, 2019: 10
                next = driver.find_element_by_xpath("//*[@id='_ctl0_cphContent_grd1_DXPagerBottom']/a[" + str(option_num) + "]")   
            except:
                pass
        if j >= 1:
            try: #If 2020: 6, 2019: 10
                next = driver.find_element_by_xpath("//*[@id='_ctl0_cphContent_grd1_DXPagerBottom']/a[" + str(option_num + 2) + "]") 
            except:
                pass
    
        file = open("Data//data" + str(j) + ".txt", 'w')
        wait.until(lambda driver: driver.find_elements_by_id("_ctl0_cphContent_grd1_DXTitle"))
        for i in range(0,100):
            print(z)

            row = driver.find_element_by_id("_ctl0_cphContent_grd1_DXDataRow" + str(z))

            # try:
            #     row = driver.find_element_by_id("_ctl0_cphContent_grd1_DXDataRow" + str(z))
            # except:
            #     print("Error")
            #     driver.quit()
            #     return 0
            file.write(row.get_attribute('innerHTML'))
            z = z + 1
        file.close()
        next.send_keys("\n")
    return 1

    




status = login()
status = goToResults(status)
status = scrapeResults(status)


