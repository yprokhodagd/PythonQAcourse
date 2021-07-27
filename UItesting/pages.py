from selenium.webdriver.common.by import By
from UItesting.actions import BaseActions


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    ABOUT_LINK_XPATH = By.XPATH, "//a[contains(text(),'About')]"
    TOPICS_FILTER = By.XPATH, "//span[contains(.,'All topics')]"
    ALL_TOPICS = By.CSS_SELECTOR, "#topiclist .showall"
    CLOUD_TOPIC = By.XPATH, "//div[@id='topiclist']/div/span[6]"
    CLOUD_ARTICLES = By.XPATH, '//*[@id="woe"]/section[8]/div/div//article'
    ALL_ARTICLES = By.XPATH, '//*[@id="woe"]/section[4]/div/div//article'

    GET_IN_TOUCH_BTN = By.XPATH, "//div[@id='woe']/gd-header/header/div/div/gd-button/a/span"

    def count_articles(self):
        self.articles_list = self.driver.find_elements(*self.CLOUD_ARTICLES)
        assert len(self.articles_list) > 1

    def get_first_article_name(self):
        self.first_article_name = self.articles_list[0].text

    def get_second_article_name(self):
        self.all_articles_list = self.driver.find_elements(*self.ALL_ARTICLES)
        self.second_article_name = self.all_articles_list[0].text

    def compare_two_articles(self):
        print(self.first_article_name, self.second_article_name)
        assert self.first_article_name != self.second_article_name

    def count_second_articles(self):
        assert len(self.all_articles_list) > 1

    def click_on_get_in_touch(self):
        self.driver.find_element(*self.GET_IN_TOUCH_BTN).click()


class ContactUsPage(BasePage):
    TITLE = "Contact us"
    INPUT = By.XPATH, "//input[@type='text']"
    DROP_DOWN = By.XPATH, "//gd-select/div"
    DROP_DOWN_ONLINE_ADS = By.XPATH, "//gd-select-option[4]"
    TERMS_CHBX = By.XPATH, "//div/label/span"
    ALLOW_CHBX = By.XPATH, "//div[2]/label/span"
    CONTACT_BTN = By.XPATH, "//gd-button[@type='submit']"

    def check_page_title(self):
        assert self.driver.title == self.TITLE

    def check_contact_button_is_disabled(self):
        ba = BaseActions(self.driver)
        button = ba.wait_till_element_is_visible(*self.CONTACT_BTN)
        assert button.is_enabled()


class AboutPage(BasePage):
    LEONARD_LIVSCHITZ_LINK = By.XPATH, "//gd-person-head/div/div[2]"
    LEONARD_LIVSCHITZ_BIO = By.XPATH, "//gd-wysiwyg-content/p/span"
    LEONARD_LIVSCHITZ_BIO_TEXT = 'a director of Grid Dynamics’ board of directors since 2006 and the Chief Executive ' \
                                 'Officer of Grid Dynamics since 2014. '

    def check_text_in_bio(self):
        text = self.driver.find_element(*self.LEONARD_LIVSCHITZ_BIO).text
        assert self.LEONARD_LIVSCHITZ_BIO_TEXT in text
