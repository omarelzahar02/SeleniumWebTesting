# '
# User Story 1: Successful Return to Contact List
# As a registered user, I want to be able to return to the contact list from the contact details page so that I can easily navigate between different contacts.

# Acceptance Criteria:
# 1. When I am logged in and on the contact list page, I should be able to see a list of my contacts.
# 2. When I click on a contact, I should be redirected to the contact details page.
# 3. On the contact details page, a return button should be visible.
# 4. When I click on the return button, I should be redirected back to the contact list page.
# '

Feature: Return to Contact List

    Scenario: View contact details and return to contact list
        Given I am signed in
        And I am on the contact list page
        When I click on any contact
        Then the contact details should appear
        And I should see a return button
        When I click on the return button
        Then I should return to the contact list page