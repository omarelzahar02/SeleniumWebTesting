Feature: Add Contact

    # User Story: Add New Contact
    # As a registered user,
    # I want to add a new contact with their full details,

    Scenario Outline: User adds a new contact
        Given the user is logged in
        And the user is on the contacts page
        When the user clicks the add a new contact button
        And the user enters the following details to add a new contact
            | first_name | last_name | DOB   | email   | phone_number | address 1 | address 2 | city   | state   | postal_code | country   |
            | <first>    | <last>    | <dob> | <email> | <phone>      | <addr1>   | <addr2>   | <city> | <state> | <postal>    | <country> |

        And the user clicks the submit button
        Then the new contact should be added to the contact list
        #And the contact with first name <first> and last name <last> should appear in the contact list

        Examples:
            | first   | last     | dob        | email               | phone      | addr1 | addr2 | city        | state          | postal | country |
            | Omar    | Elzahar  | 2000-01-01 | omar@example.com    | 1864114868 | 17 St | 83 St | Cairo       | Tagamo3        | 10001  | Egypt   |
            | Abdullah| Ayman    | 1990-01-01 | abdullah@example.com| 1234567890 | 17 St | 83 St | Cairo       | Maadi          | 10001  | Egypt   |
            | Youssef | Hassan   | 1992-02-02 | darwish@example.com | 0987654321 | 5678  |       | Giza        | Haram          | 90001  | Egypt   |
            | Yehia   | fawzy    |            |                     |            |       |       |             |                |        |         |
    
    # User Story: Add New Contact with Wrong Date Format
    # As a registered user,
    # I want to see an error message when I enter a birth date in the wrong format,
    # so that I can understand the correct date format.

    Scenario Outline: User adds a new contact with wrong date format
        Given the user is logged in
        And the user is on the contacts page
        When the user clicks the add a new contact button
        And the user enters the following details to add a new contact
            | first_name | last_name | DOB   | email   | phone_number | address 1 | address 2 | city   | state   | postal_code | country   |
            | <first>    | <last>    | <dob> | <email> | <phone>      | <addr1>   | <addr2>   | <city> | <state> | <postal>    | <country> |

        And the user clicks the submit button
        Then the user should see an birth date error message

        Examples:
            | first   | last     | dob      | email               | phone      | addr1 | addr2 | city  | state | postal | country |
            | Omar    | Elzahar | 01-01-90  | omar@example.com | 1234567890    | 17 St | 83 St | Cairo | Cairo | 10001  | Egypt   |
    
    # User Story: Add New Contact with Wrong Email Format
    # As a registered user,
    # I want to see an error message when I enter an email in the wrong format,
    # so that I can understand the correct email format.

    Scenario Outline: User adds a new contact with wrong email format
        Given the user is logged in
        And the user is on the contacts page
        When the user clicks the add a new contact button
        And the user enters the following details to add a new contact
            | first_name | last_name | DOB   | email   | phone_number | address 1 | address 2 | city   | state   | postal_code | country   |
            | <first>    | <last>    | <dob> | <email> | <phone>      | <addr1>   | <addr2>   | <city> | <state> | <postal>    | <country> |

        And the user clicks the submit button
        Then the user should see an email validation error message

        Examples:
            | first   | last     | dob        | email           | phone      | addr1 | addr2 | city  | state | postal | country |
            | Omar    | Elzahar  | 1990-01-01 | omargmail.com     | 1234567890 | 17 St | 83 St | Cairo | Cairo | 10001  | Egypt   |

    # User Story: Cancel Adding New Contact
    # As a registered user,
    # I want to cancel the action of adding a new contact after entering their details,
    # so that no new contact is added to my contact list.
    
    Scenario Outline: User cancels adding a new contact
        Given the user is logged in
        And the user is on the contacts page
        When the user clicks the add a new contact button
        And the user enters the following details to add a new contact
            | first_name | last_name | DOB   | email   | phone_number | address 1 | address 2 | city   | state   | postal_code | country   |
            | <first>    | <last>    | <dob> | <email> | <phone>      | <addr1>   | <addr2>   | <city> | <state> | <postal>    | <country> |

        But the user clicks the cancel button
        Then the new contact should not be added to the contact list

        Examples:
            | first   | last     | dob        | email               | phone      | addr1 | addr2 | city  | state | postal | country |
            | Omar    | Elzahar  | 1990-01-01 | omar@example.com | 1234567890 | 17 St | 83 St | Cairo | Cairo | 10001  | Egypt   |