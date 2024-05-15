
User Story 1: Successful Return to Contact List
As a registered user, I want to be able to return to the contact list from the contact details page so that I can easily navigate between different contacts.
definition of done: when i go back to contact list page

Feature: Return to Contact List

    User Story 1: Successful Return to Contact List
    As a registered user, 
    I want to be able to return to the contact list from the contact details page 
    so that I can easily navigate between different contacts.
    definition of done: I successfully return to the contact list page from the contact details page

    Scenario: View contact details and return to contact list
        Given I am signed in
        And I am on the contact list page
        When I click on any contact
        Then the contact details should appear
        And I should see a return button
        When I click on the return button
        Then I should return to the contact list page