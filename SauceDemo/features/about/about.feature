Feature: About

    Scenario: Successful About redirection
        Given I am logged in
        When I click on the more options button
        Then About button should be visible
        When I click on the About button
        Then I am redirected to the About page
