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