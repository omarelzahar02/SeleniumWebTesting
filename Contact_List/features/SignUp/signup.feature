Feature: Sign Up

    Scenario: Successful sign up
        Given new user want to use the contact list app
        And the user is on the sign up page
        When the user tries to sign up with first name, last name, email and password
        Then the sign up should be successful


    Scenario Outline: Unsuccessful sign up
        Given a user tries to sign up again with <credential>
        When the user enters <credential>
        Then a warning appears that <message>

        Examples:
            | credential                   | message                     |
            | the same email               | the email is already in use |
            | a password that is too short | the password is too short   |
    
