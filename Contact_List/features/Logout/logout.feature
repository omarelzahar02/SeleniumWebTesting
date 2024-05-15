
User Story 1: Successful Logout
As a registered user, I want to be able to log out of my account so that I can ensure my account is secure when I'm not using it.
definition of done: when im in login page again
Feature: Logout
    User Story 1: Successful Logout
    As a registered user, 
    I want to be able to log out of my account 
    so that I can ensure my account is secure when I'm not using it.
    definition of done: i logout of my account and i am redirected to the login page
    
    Scenario: Successful logout
        Given a registered user is already logged in
        And the user is on the contact list page
        When the user clicks the logout button
        Then the user should be logged out and redirected to the login page