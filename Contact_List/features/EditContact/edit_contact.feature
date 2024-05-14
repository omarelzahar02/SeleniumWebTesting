Feature: Edit Contact

    # User Story 1: Successful Login for Accessing Edit Contact Feature
    # As a registered user, User will be able to log in successfully to access the edit contact feature.
    # Then User will be able to see all his contacts in his contacts list.
    # User will choose the desired contact that he want to edit.
    # All the contact details will be displayed in a seperate page.
    # User will choose the feature which will be edit contact.
    # So that User can update the details of existing contacts with valid contact details in his contact list.
    # User will press save for the contact to be updated.


    Scenario Outline: User edits an existing contact
        Given the user is logged in
        And the user is on the contact list page
        When the user clicks on the row for the contact with first name <first> and last name <last>
        Then the user is navigated to the contact details page
        When the user clicks the edit button
        Then the user is navigated to the edit contact page with the contact's details filled in
        And the user updates the following details
            | first_name | last_name | DOB   | email   | phone_number | address 1 | address 2 | city   | state   | postal_code | country   |
            | <new_first>| <new_last>| <new_dob> | <new_email> | <new_phone> | <new_addr1> | <new_addr2> | <new_city> | <new_state> | <new_postal> | <new_country> |
        And the user clicks the submit button
        Then the user is navigated back to the contact details page
        And the contact should be updated in the contact list

        Examples:
        | first     | last    | new_first    | new_last     | new_dob       | new_email | new_phone | new_addr1 | new_addr2 | new_city | new_state | new_postal | new_country |
        | Hussein   | Mostafa | Hussein      | Mostafa      | 2000-09-29    | jane.doe@example.com | 1234567890 | 123 New Street | Apt 4B | New City | New State | 12345 | New Country |


    # User Story 2: Successful Login for Accessing Edit Contact Feature with Invalid Data
    # As a registered user, User will be able to log in successfully to access the edit contact feature.
    # Then User will be able to see all his contacts in his contacts list.
    # User will choose the desired contact that he want to edit.
    # All the contact details will be displayed in a seperate page.
    # User will choose the feature which will be edit contact.
    # So that User can update the details of existing contacts with invalid contact details in his contact list.
    # User will press save for the contact to be updated.
    # User will see the error message for the invalid data.
    # error message for email validation and birthdate validation.

    Scenario Outline: User tries to edit a contact with invalid data
        Given the user is logged in
        And the user is on the contact list page
        When the user clicks on the row for the contact with first name <first> and last name <last>
        Then the user is navigated to the contact details page
        When the user clicks the edit button
        Then the user is navigated to the edit contact page with the contact's details filled in
        And the user updates the following details
            | first_name | last_name | DOB   | email   | phone_number | address 1 | address 2 | city   | state   | postal_code | country   |
            | <new_first>| <new_last>| <new_dob> | <new_email> | <new_phone> | <new_addr1> | <new_addr2> | <new_city> | <new_state> | <new_postal> | <new_country> |
        And the user clicks the submit button
        Then the user should see the error message <error_message>
    
        Examples:
        | first     | last    | new_first | new_last | new_dob       | new_email            | new_phone  | new_addr1      | new_addr2 | new_city | new_state | new_postal | new_country | error_message |
        | Omar      | Elzahar | Jane      | Doe      | 20/9/5        | jane.doe@example.com | 1234567890 | 123 New Street | Apt 4B    | New City | New State | 12345      | New Country | Validation failed: birthdate: Birthdate is invalid |
        | Youssef   | Hassan  | Moaaz      | Tarek    | 2000-09-29    | jane.doeexample.com | 1234567890 | 123 New Street | Apt 4B | New City | New State | 12345 | New Country | Validation failed: email: Email is invalid |

    # User Story 3: Successful Login for Accessing Edit Contact Feature with Cancel Button
    # As a registered user, User will be able to log in successfully to access the edit contact feature.
    # Then User will be able to see all his contacts in his contacts list.
    # User will choose the desired contact that he want to edit.
    # All the contact details will be displayed in a seperate page.
    # User will choose the feature which will be edit contact.
    # So that User can update the details of existing contacts with valid contact details in his contact list.
    # User decides to cancel the editing of the contact, so he will press on cancel button.
    # User will see the contact details without any changes.


    Scenario Outline: User cancels editing a contact
        Given the user is logged in
        And the user is on the contact list page
        When the user clicks on the row for the contact with first name <first> and last name <last>
        Then the user is navigated to the contact details page
        When the user clicks the edit button
        Then the user is navigated to the edit contact page with the contact's details filled in
        And the user updates the following details
            | first_name | last_name | DOB   | email   | phone_number | address 1 | address 2 | city   | state   | postal_code | country   |
            | <new_first>| <new_last>| <new_dob> | <new_email> | <new_phone> | <new_addr1> | <new_addr2> | <new_city> | <new_state> | <new_postal> | <new_country> |
        But the user clicks the cancel button
        Then the user is navigated back to the contact details page
        And the contact should not be updated in the contact details page

        Examples:
        | first     | last    | new_first | new_last | new_dob       | new_email            | new_phone  | new_addr1      | new_addr2 | new_city | new_state | new_postal | new_country | error_message |
        | Omar      | Elzahar | Jane      | Doe      | 20/9/5        | jane.doe@example.com | 1234567890 | 123 New Street | Apt 4B    | New City | New State | 12345      | New Country | Validation failed: birthdate: Birthdate is invalid |

    # Scenario Outline: User deletes an existing contact
    #     Given the user is logged in
    #     And the user is on the contact list page
    #     When the user clicks on the row for the contact with first name <first> and last name <last>
    #     Then the user is navigated to the contact details page
    #     When the user clicks the delete button
    #     Then a confirmation dialog should appear
    #     When the user confirms the deletion
    #     Then the user is navigated back to the contact list page
    #     And the contact with first name <first> and last name <last> should not be in the contact list

    #     Examples:
    #     | first     | last    |
    #     | Hussein   | Mostafa |
