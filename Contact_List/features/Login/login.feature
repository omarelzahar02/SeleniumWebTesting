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