Feature: About

    User Story 1: Successful access of About Page
    As a registered user, 
    I want to be able to access the About page 
    so that I can learn more about the platform.
    definition of done: i access the about page successfully

    Scenario: Successful About redirection
        Given I am logged in
        When I click on the more options button
        Then About button should be visible
        When I click on the About button
        Then I am redirected to the About page
