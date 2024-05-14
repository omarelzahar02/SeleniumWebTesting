
# User Story 1: Successful Logout
# As a registered user, I want to be able to log out of my account so that I can ensure my account is secure when I'm not using it.

# Acceptance Criteria:
# 1. When I am logged in, a more options button should be visible.
# 2. When I click on the more options button, a Logout button should be visible.
# 3. When I click on the Logout button, I should be logged out.
# 4. After I have logged out, I should be redirected to the login page.

Feature: Logout

    Scenario: Successful Logout
        Given I am logged in
        When I click on the more options button
        Then Logout button should be visible
        When I click on the logout button
        Then I should be logged out
