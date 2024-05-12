Feature: Add Contact

    Scenario Outline: User adds a new contact with full details
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
            | first   | last     | dob        | email               | phone      | addr1 | addr2 | city        | state | postal | country |
            | Hussein | Mosatafa | 1990-01-01 | hussein@example.com | 1234567890 | 17 St | 83 St | New York    | NY    | 10001  | USA     |
            | Youssef | Hassan   | 1992-02-02 | darwish@example.com | 0987654321 | 5678  |       | Los Angeles | CA    | 90001  | USA     |

    
    # Scenario Outline: User adds a new contact with only first name and last name
    #     Given the user is logged in
    #     And the user is on the contacts page
    #     When the user clicks the add a new contact button
    #     And the user enters the following details to add a new contact
    #         | first_name | last_name |
    #         | <first>    | <last>    |

    #     And the user clicks the submit button
    #     Then the new contact should be added to the contact list

    #     Examples:
    #         | first   | last     |
    #         | Hussein | Mosatafa |
    #         | Youssef | Hassan   |