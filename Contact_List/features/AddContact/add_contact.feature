Feature: Add Contact

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
            | Abdullah| Ayman    | 1990-01-01 | abdullah@example.com| 1234567890 | 17 St | 83 St | Cairo       | Maadi          | 10001  | Egypt   |
            | Youssef | Hassan   | 1992-02-02 | darwish@example.com | 0987654321 | 5678  |       | Giza        | Haram          | 90001  | Egypt   |
            | Ahmed   | Ali      |            |                     |            |       |       |             |                |        |         |
    
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
            | Hussein | Mosatafa | 01-01-90 | hussein@example.com | 1234567890 | 17 St | 83 St | Cairo | Cairo | 10001  | Egypt   |

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
            | Hussein | Mosatafa | 1990-01-01 | husseingmail.com     | 1234567890 | 17 St | 83 St | Cairo | Cairo | 10001  | Egypt   |