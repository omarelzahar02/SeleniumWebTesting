Feature: Logout

    Scenario: Successful logout
        Given a registered user is already logged in
        And the user is on the contact list page
        When the user clicks the logout button
        Then the user should be logged out and redirected to the login page