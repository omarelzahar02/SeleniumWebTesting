Feature: Return to Contact List

    Scenario: View contact details and return to contact list
        Given I am signed in
        And I am on the contact list page
        When I click on any contact
        Then the contact details should appear
        And I should see a return button
        When I click on the return button
        Then I should return to the contact list page