Feature: Sign Up

    # User Story: Successful Sign Up
    # As a new user,
    # User want to sign up with his credentials ,
    # so that I can use the contact list app.

    Scenario: Successful sign up
        Given new user want to use the contact list app
        And the user is on the sign up page
        When the user tries to sign up with first name, last name, email and password
        Then the sign up should be successful

    # User Story: Unsuccessful Sign Up
    # As a new User,
    # User want to receive a warning when I try to sign up with an email that's already in use or a password that's too short,
    # so that User can understand the sign up requirements.

    Scenario Outline: Unsuccessful sign up
        Given a user tries to sign up again with <credential>
        When the user enters <credential>
        Then a warning appears that <message>

        Examples:
            | credential                   | message                     |
            | the same email               | the email is already in use |
            | a password that is too short | the password is too short   |
    
