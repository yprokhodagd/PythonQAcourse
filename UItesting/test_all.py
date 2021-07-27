from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from UItesting.pages import HomePage, AboutPage, ContactUsPage
from UItesting.actions import BaseActions


class Test1:
    def setup(self):
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)  # Chrome stays opened
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://blog.griddynamics.com/')

    def test_1(self):
        """
        Case #1:
        Open https://blog.griddynamics.com
        Go to About page
        Find Leonard Livschitz and click on the name
        Verify that information about Leonard has appeared. The text “director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014” is visible.
        """
        ba = BaseActions(self.driver)
        hp = HomePage(self.driver)
        ap = AboutPage(self.driver)
        ba.find_element(*hp.ABOUT_LINK_XPATH).click()
        ba.find_element(*ap.LEONARD_LIVSCHITZ_LINK).click()
        ap.check_text_in_bio()

    def test_2(self):
        """
        Open https://blog.griddynamics.com
        Click ‘filter’ (check it’s visible and available)
        Filter by Cloud and DevOps topic
        Check there is more than 1 article
        Reset all filters
        Check the first article in the list is different than in step 4 and check there is more than 1 article.
        """
        ba = BaseActions(self.driver)
        hp = HomePage(self.driver)
        ba.windows_scroll(0, 400)
        filter_drop_down = ba.wait_till_element_is_clickable(*hp.TOPICS_FILTER)
        sleep(2)  # can't remove((

        # change topic: cloud etc.
        filter_drop_down.click()
        ba.wait_till_element_is_clickable(*hp.CLOUD_TOPIC).click()
        hp.count_articles()
        hp.get_first_article_name()

        # change topic: all topics
        filter_drop_down.click()
        ba.wait_till_element_is_clickable(*hp.ALL_TOPICS).click()
        sleep(2)
        hp.get_second_article_name()
        hp.compare_two_articles()
        hp.count_second_articles()

    def test_3(self):
        """
        Case #3:
        Open https://blog.griddynamics.com
        Click on Get In Touch button
        Ensure page Contact Us opened
        Fill in the following:
        First Name = Anna, Last Name = Smith
        email = annasmith@griddynamics.com
        select  How did you hear about us? = Online Ads
        Click on checkbox “I have read and accepted the Terms & Conditions and Privacy Policy”
        Click on checkbox “I allow Grid Dynamics to contact me”
        Ensure Contact button is inactive
        """
        ba = BaseActions(self.driver)
        hp = HomePage(self.driver)
        cu = ContactUsPage(self.driver)
        sleep(3)
        hp.click_on_get_in_touch()

        """Ensure page Contact Us opened"""
        cu.check_page_title()

        """ Fill in the following:
        First Name = Anna, Last Name = Smith
        email = annasmith@griddynamics.com"""
        input_elements = ba.wait_till_elements_are_visible(*cu.INPUT)
        first_name = input_elements[0]
        last_name = input_elements[1]
        email = input_elements[2]
        first_name.click()
        ba.type_text(first_name, 'Anna')
        last_name.click()
        ba.type_text(last_name, 'Smith')
        email.click()
        ba.type_text(email, 'annasmith@griddynamics.com')

        # tmp
        asd = ba.wait_till_element_is_visible(By.XPATH, '//textarea')
        asd.click()
        ba.type_text(asd, 'asdfasdfasdf')

        """select  How did you hear about us? = Online Ads"""
        selection = ba.wait_till_element_is_visible(*cu.DROP_DOWN)
        selection.click()
        online_ads = ba.wait_till_element_is_visible(*cu.DROP_DOWN_ONLINE_ADS)
        online_ads.click()

        """Click on checkbox “I have read and accepted the Terms & Conditions and Privacy Policy”
        Click on checkbox “I allow Grid Dynamics to contact me”"""
        chbx1 = ba.wait_till_element_is_visible(*cu.TERMS_CHBX)
        chbx2 = ba.wait_till_element_is_visible(*cu.ALLOW_CHBX)
        chbx1.click()
        chbx2.click()

        """Ensure Contact button is inactive"""
        cu.check_contact_button_is_disabled()
