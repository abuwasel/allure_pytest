from Functions import *
from selectors_dic import selector

@pytest.fixture
def url():
    return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

@pytest.fixture
def init_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def selectors():
    return selector

@allure.epic("Login")
@allure.story("Login & deposit, withdrawal, balance Functionality")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
class TestDemo:

    @allure.title("Check the balance of the account is 750")
    @allure.description("Enter the bank as a user, make a deposit of 1000 NIS and a withdrawal of 250, check that the balance of the account is 750")
    @allure.label("owner", "Ibrahim Abu Wasel")
    def test_login_deposit_withdraw_check_balance(self, url, selectors, init_driver):
        """
        Enter the bank as a user,
        make a deposit of 1000,
        withdrawal of 250,
        check that the balance of the account is 750.

        Expected: the balance is 750
        """
        driver = init_driver
        time.sleep(2)
        # List of selector keys in the order of execution
        actions = [
            ('Customer Login btn', None),
            ('Harry Potter', None),
            ('Login btn', None),
            ('Deposit btn', None),
            ('amount input', 1000),
            ('Deposit submit', None),
            ('Withdrawl btn', None),
            ('Withdrawl amount input', 250),
            ('Withdrawl submit', None)
        ]

        for action in actions:
            if action[1] is not None:
                handle_element(driver, selectors[action[0]], action[1])
            else:
                handle_element(driver, selectors[action[0]])
            time.sleep(1)

        time.sleep(2)
        expected_balance = 7500
        actual_balance = get_items_as_number(driver, selectors['Balance'])
        try:
            assert actual_balance == expected_balance, f'Expected Balance: {expected_balance}, but got: {actual_balance}'
        except AssertionError as e:
            capture_a_screenshot_and_save_it(driver)
            raise e