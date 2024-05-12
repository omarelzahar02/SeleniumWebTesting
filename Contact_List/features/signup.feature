Feature: Sign Up

    Scenario: Successful sign up
        Given new user want to use the contact list app
        And the user is on the sign up page
        When the user tries to sign up with first name, last name, email and password
        Then the sign up should be successful

        

    # Scenario: Unsuccessful sign up
    #     Given a user exists with username 
    #     When the user tries to sign up with username and password
    #     Then the sign up should be unsuccessful