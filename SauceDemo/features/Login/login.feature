Feature: Login to SauceDemo

    Scenario Outline: Successful login with predefined users
        Given a user "<username>" is on the SauceDemo login page
        When the user logs in with username "<username>" and the predefined password
        Then the login should be successful and the user sees the product page

        Examples:
            | username      |
            | standard_user |
            | problem_user  |
            | error_user    |
            | visual_user   |

    Scenario: Unsuccessful login with incorrect password
        Given a user "standard_user" is on the SauceDemo login page
        When the user attempts to log in with an incorrect password
        Then a warning should appear that the password is incorrect

    Scenario: Unsuccessful login with only username entered
        Given a user "standard_user" is on the SauceDemo login page
        When the user enters only their username and attempts to log in
        Then a warning should appear that the password cannot be empty

    Scenario: Unsuccessful login with only password entered
        Given a user "standard_user" is on the SauceDemo login page
        When the user enters only their password and attempts to log in
        Then a warning should appear that the username cannot be empty

# User Story 1: Successful Login for Different User Types
# As a user with a predefined account type,
# I want to log in using my specific username and the shared password,
# So that I can access the product page specific to my account type.

# Acceptance Criteria:

# Given I am on the SauceDemo login page,
# When I enter my predefined username (e.g., standard_user, problem_user, error_user, visual_user),
# And I enter the correct shared password,
# Then I am logged in successfully and taken to the product page.


# User Story 2: Unsuccessful Login with Incorrect Password
# As a user,
# I want the system to validate my password upon login,
# So that an incorrect password entry prevents unauthorized access.

# Acceptance Criteria:

# Given I am on the SauceDemo login page as "standard_user",
# When I enter an incorrect password,
# Then I am informed that the password is incorrect.

# User Story 3: Unsuccessful Login with Only Username Entered
# As a user,
# I want to be informed when I forget to enter my password,
# So that I can be reminded to provide it to complete my login.

# Acceptance Criteria:

# Given I am on the SauceDemo login page as "standard_user",
# When I enter my username but do not enter any password,
# Then I am prompted that the password field cannot be empty.

# User Story 4: Unsuccessful Login with Only Password Entered
# As a user,
# I want the system to prompt me if I forget to enter my username,
# So that I can be reminded to provide it to access my account.
# Acceptance Criteria:

# Given I am on the SauceDemo login page as "standard_user",
# When I enter my password but do not enter any username,
# Then I am alerted that the username field cannot be empty.