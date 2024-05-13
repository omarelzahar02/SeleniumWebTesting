Feature: Login

    Scenario: Successful login
        Given a registered user wants to access the contact list app
        And the user is on the login page
        When the user logs in with a valid email and password
        Then the login should be successful and the user sees the main contact list

    Scenario: Unsuccessful login with incorrect password**
        Given a registered user is on the login page
        When the user tries to log in with an incorrect password
        Then a warning should appear that the password is incorrect

    Scenario: Unsuccessful login with unregistered email
        Given a user is on the login page
        When the user tries to log in with an email that is not registered
        Then a warning should appear that the account does not exist

# User Story 1: Successful Login for Different User Types
# As a user with a predefined account type,
# I want to log in using my specific username and the shared password,
# So that I can access the product page specific to my account type.

# User Story 2: Unsuccessful Login with Incorrect Password
# As a user,
# I want the system to validate my password upon login,
# So that incorrect password entries prevent access to ensure security.

# User Story 3: Unsuccessful Login with Only Username Entered
# As a user,
# I want to be informed when I forget to enter my password,
# So that I can be reminded to provide it to complete my login.

# User Story 4: Unsuccessful Login with Only Password Entered
# As a user,
# I want the system to prompt me if I forget to enter my username,
# So that I can be reminded to provide it to access my account.
