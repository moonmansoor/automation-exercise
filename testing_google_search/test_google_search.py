from bs4 import BeautifulSoup
from bs4.element import Tag

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class _AbstractTestCase(object):
    """
    Abstract Selenium test case class that Selenium tests must
    inherit from.
    """

    @staticmethod
    def _get_driver_options():
        """Return options for Google Chrome WebDriver.
        :return: An instance of ChromeOptions() with additional
        arguments.
        """
        options = webdriver.ChromeOptions()
        return options

    @classmethod
    def setup_class(cls):
        """ Set up Google Chrome WebDriver"""
        cls.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=cls._get_driver_options()
        )
        cls.driver.set_window_position(0, 0)


class TestGoogle(_AbstractTestCase):
    def test_google_search(self):
        """go the google page and do keyword search"""
        self.url = 'https://www.google.com/'
        self.driver.get(self.url)
        self.driver.find_element(
            By.NAME,
            "q"
        ).click()
        self.driver.find_element(
            By.NAME,
            "q"
        ).send_keys('Halal Food in KL')
        self.driver.find_element(
            By.NAME,
            "q"
        ).send_keys(Keys.RETURN)

    def test_get_search_result(self):
        """Get the result and massage the result data"""
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        result_div = soup.find_all('div', attrs={'class': 'g'})

        links = []
        titles = []
        for index, result in enumerate(result_div):
            link = result.find('a', href=True)
            title = None
            title = result.find('h3')

            if isinstance(title, Tag):
                title = title.get_text()

            # Check that link and title is not empty
            if link != '' and title != '':
                links.append(link['href'])
                titles.append(title)

            if index == 4:
                break

        # create a txt file
        f = open('Search Result.txt', 'w')
        for index, title in enumerate(titles):
            for index_2, link in enumerate(links):
                if index == index_2:
                    # arrange the title and link and write it in the txt file
                    f.write(f'{index+1}:- {title}, {link}' + '\n')
                    print(f'{index+1}:- {title}, {link}' + '\n')

        #close the file
        f.close()
        self.driver.quit()
