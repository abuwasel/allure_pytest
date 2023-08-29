# allure_pytest

# To run test and create report directory
```pytest --alluredir=allure_report/ test_demo_report.py```

```pytest --alluredir=allure_report/ test_demo_report_with_selenium.py```

# To run and open allure report
```allure serve "C:\Users\User\PycharmProjects\allure_pytest\allure_report"```

```allure serve "C:\Users\User\PycharmProjects\allure_pytest\allure_report"```

# How to Install Allure on Windows OS
https://www.youtube.com/watch?v=xdjN-4UxL1c

# Download allure framework
https://github.com/allure-framework/allure2

# Test severity
```
import allure

@allure.epic("Workspaces")
@allure.story("WorkSpaces Creation and Editing Functionality")
@allure.severity(allure.severity_level.NORMAL)
class TestWorkspaces(BaseTest):

      @allure.title("Create new workspace test")
      @allure.description("Create new Workspace")
      def test_severity():
           pass
```
Allure supports next severity levels: ```TRIVIAL```, ```MINOR```, ```NORMAL```, ```CRITICAL``` , ```BLOCKER```. By default, all tests marks with NORMAL severity.

