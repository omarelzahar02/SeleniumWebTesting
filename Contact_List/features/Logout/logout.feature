# '
# User Story 1: Successful Logout
# As a registered user, I want to be able to log out of my account so that I can ensure my account is secure when I'm not using it.

# Acceptance Criteria:
# 1. When I am logged in, a logout button should be visible.
# 2. When I click on the Logout button, I should be logged out.
# 3. After I have logged out, I should be redirected to the login page.
# '
Feature: Logout

    Scenario: Successful logout
        Given a registered user is already logged in
        And the user is on the contact list page
        When the user clicks the logout button
        Then the user should be logged out and redirected to the login page