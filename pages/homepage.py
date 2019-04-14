class Homepage:
    def __init__(self,driver):
        self.driver=driver
        self.logout="//*[text()='Logout']"

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout).click()


