# User Story 1: Successful access of About Page
# As a registered user, I want to be able to access the About page so that I can learn more about the platform.

# Acceptance Criteria:
# 1. When I am logged in, a more options button should be visible.
# 2. When I click on the more options button, an About button should be visible.
# 3. When I click on the About button, I should be redirected to the About page.


Feature: About

    Scenario: Successful About redirection
        Given I am logged in
        When I click on the more options button
        Then About button should be visible
        When I click on the About button
        Then I am redirected to the About page
