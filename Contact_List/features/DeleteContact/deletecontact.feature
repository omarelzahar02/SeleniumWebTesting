User Story 1: Successful Delete of a Contact
As a registered user, I want to be able to delete a contact so that I can manage my contact list effectively.
definition of done: when contact does not appear in contact list

Feature: Delete Contact
    User Story 1: Successful Delete of a Contact
    As a registered user, 
    I want to be able to delete a contact 
    so that I can manage my contact list effectively.
    definition of done: I successfully delete a contact from the contact list

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
            | first    | last    | dob        | email              | phone        | addr1       | addr2  | city    | state | postal | country |
            | Youssef  | Hassan  | 01/01/2000 | john.doe@email.com | 123-456-7890 | 123 Main St | Apt 4B | Anytown | NY    | 12345  | USA     |