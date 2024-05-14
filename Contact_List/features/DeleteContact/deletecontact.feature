'
User Story 1: Successful Delete of a Contact
As a registered user, I want to be able to delete a contact so that I can manage my contact list effectively.

Acceptance Criteria:
1. When I am logged in and my contact list is not empty, I should be able to see a list of my contacts.
2. When I click on a contact, I should be redirected to the contact details page.
3. On the contact details page, a delete button should be visible.
4. When I click on the delete button, a confirmation prompt should appear.
5. When I click on the confirm button in the prompt, I should be redirected back to the contact list page.
6. The deleted contact should no longer appear in my contact list.
'

Feature: Delete Contact

    Scenario Outline: Successfully delete a contact
        Given I am logged in
        And Contact list is not empty
        Given I have a contact with the name "<first> <last>"
        When I click on the contact
        Then Contact details should be displayed page
        When I click on the delete button
        Then Website displays a confirmation prompt
        When I click on the confirm button
        Then I am redirected to the contact list page
        And the contact should be deleted

        Examples: 
            | first | last | dob        | email          | phone         | addr1       | addr2 | city   | state | postal | country |
            | John  | Doe  | 01/01/2000 | john.doe@email.com | 123-456-7890 | 123 Main St | Apt 4B | Anytown | NY    | 12345  | USA     |