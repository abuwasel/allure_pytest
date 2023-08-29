from Functions import *

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
    return {
        'Customer Login btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
        'Bank Manager Login btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
        'Harry Potter': '#userSelect > option:nth-child(3)',
        'Login btn': 'body > div > div > div.ng-scope > div > form > button',
        'Deposit btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
        'amount input': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
        'Deposit submit': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
        'Balance': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)',
        'Bank Manager btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
        'Customers btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
        'Delete btn': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > button',
        'Add Customer btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)',
        'First Name input': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input',
        'Last Name input': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input',
        'Post Code input': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input',
        'Add Customer submit': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button',
        'Withdrawl btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
        'Withdrawl amount input': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
        'Withdrawl submit': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
        'Transactions btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
        'Transactions table': 'body > div > div > div.ng-scope > div > div:nth-child(2) > table > tbody',
        'Transactions Back': 'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)',
        'Customers table': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody'
        }

@allure.epic("Login")
@allure.story("Login & deposit, withdrawal, balance Functionality")
@allure.severity(allure.severity_level.CRITICAL)
# Allure supports next severity levels: TRIVIAL, MINOR, NORMAL, CRITICAL , BLOCKER. By default, all tests marks with NORMAL severity.
class TestDemo:

    @allure.title("Check the balance of the account is 750")
    @allure.description("Enter the bank as a user, make a deposit of 1000 NIS and a withdrawal of 250, check that the balance of the account is 750")
    @allure.label("owner", "Ibrahim Abu Wasel")
    def test_login_deposit_withdraw_check_balance(self, url, selectors, init_driver):
        driver = init_driver
        time.sleep(2)
        handle_element(driver, selectors['Customer Login btn'])
        time.sleep(1)
        handle_element(driver, selectors['Harry Potter'])
        time.sleep(1)
        handle_element(driver, selectors['Login btn'])
        time.sleep(1)
        handle_element(driver, selectors['Deposit btn'])
        time.sleep(1)
        handle_element(driver, selectors['amount input'], 1000)
        time.sleep(1)
        handle_element(driver, selectors['Deposit submit'])
        time.sleep(2)
        handle_element(driver, selectors['Withdrawl btn'])
        time.sleep(1)
        handle_element(driver, selectors['Withdrawl amount input'], 250)
        time.sleep(1)
        handle_element(driver, selectors['Withdrawl submit'])
        time.sleep(2)
        expected_balance = 7500
        actual_balance = get_items_as_number(driver, selectors['Balance'])
        try:
            assert actual_balance == expected_balance, f'Expected Balance: {expected_balance}, but got: {actual_balance}'
        except AssertionError as e:
            capture_a_screenshot_and_save_it(driver)
            raise e