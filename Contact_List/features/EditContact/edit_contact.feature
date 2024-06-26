Feature: Edit Contact
    
    User Story: Edit Contact
    As a registered User,
    User want to be able to select a contact from his list,
    edit their details, and save the changes,
    so that User can keep his contacts up to date.
    definition of done: when contact details are updated in contact list


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


    User Story: Edit Contact with Invalid Data
    As a registered user,
    User edits his contact details with invalid data,
    User will see an error message,
    so that User can understand the data validation rules.
    definition of done: when error message appears on screen

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

    User Story: Edit Contact and Cancel
    As a registered User,
    User want to select a contact to edit,
    start editing their details,
    and then decide to cancel the editing,
    so that the original contact details remain unchanged.
    definition of done: when contact details are not changed in contact list


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
