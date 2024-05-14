Feature: Logout

    Scenario: Successful Logout
        Given I am logged in
        When I click on the more options button
        Then Logout button should be visible
        When I click on the logout button
        Then I should be logged out
