Feature: Complete Checkout Process

    Scenario Outline: Check whether user can complete checkout from cart
        Given User should login to swag labs using correct "<Username>" and "<Password>"
        And User clicks the add to cart buttons
        And User clicks the cart icon
        When User clicks the checkout button
        And User enters checkout information with "<FirstName>", "<LastName>", "<ZipCode>"
        And User clicks the continue button
        Then User should see the checkout overview page
        When User clicks the finish button
        Then User should see the order confirmation with "Thank you for your order!"

        Examples:
            | Username      | Password     | FirstName | LastName | ZipCode |
            | standard_user | secret_sauce | John      | Doe      | 90210   |
            | visual_user   | secret_sauce | Alice     | Johnson  | 98765   |

    Scenario Outline: Check problem user cannot checkout from cart
        Given User should login to swag labs using correct "<Username>" and "<Password>"
        And User clicks the add to cart buttons
        And User clicks the cart icon
        When User clicks the checkout button
        And User enters checkout information with "<FirstName>", "<LastName>", "<ZipCode>"
        And User clicks the continue button
        Then User should see an error message "Error: Last Name is required"
        Examples:
            | Username     | Password     | FirstName | LastName | ZipCode |
            | problem_user | secret_sauce | Jane      | Smith    | 10001   |

    Scenario Outline: Check error user cannot checkout from cart
        Given User should login to swag labs using correct "<Username>" and "<Password>"
        And User clicks the add to cart buttons
        And User clicks the cart icon
        When User clicks the checkout button
        And User enters checkout information with "<FirstName>", "<LastName>", "<ZipCode>"
        And User clicks the continue button
        Then User should see the checkout overview page
        When User clicks the finish button
        Then User should see the order confirmation with "Thank you for your order!"
        Examples:
            | Username   | Password     | FirstName | LastName | ZipCode |
            | error_user | secret_sauce | Alice     | Johnson  | 98765   |

    Scenario Outline: Check whether standard user entering missing postal code and cannot checkout from cart
        Given User should login to swag labs using correct "<Username>" and "<Password>"
        And User clicks the add to cart buttons
        And User clicks the cart icon
        When User clicks the checkout button
        And User enters checkout information with "<FirstName>", "<LastName>", "<ZipCode>"
        Then User should see an error message "Error: postal code is required"
        Examples:
            | Username      | Password     | FirstName | LastName | ZipCode |
            | standard_user | secret_sauce | John      | Doe      |         |

# User Story 1: Successful Checkout Process
# As a user,
# I want to successfully complete the checkout process after adding items to my cart,
# So that I can finalize my purchase and receive confirmation.
# Acceptance Criteria:

# Given I am logged in with a valid username (e.g., standard_user, visual_user) and password,
# And I have added items to my cart and navigated to the checkout page,
# When I enter my first name, last name, and zip code and proceed through the checkout,
# Then I should see the checkout overview page,
# And when I click the finish button,
# Then I should see an order confirmation message stating, "Thank you for your order!"

# User Story 2: Problem User Checkout Failure
# As a problem user,
# I want to be informed of required fields I might have missed during checkout,
# So that I can understand why I can't proceed with the checkout.
# Acceptance Criteria:

# Given I am logged in as "problem_user",
# And I have added items to my cart and navigated to the checkout page,
# When I enter my first name and zip code but leave the last name field blank and attempt to continue,
# Then I should see an error message stating, "Error: Last Name is required."

# User Story 3: Error User Checkout Success
# As an error user,
# I want to successfully complete my checkout despite potential system issues,
# So that I can finalize my orders like other users.
# Acceptance Criteria:

# Given I am logged in as "error_user",
# And I have added items to my cart and filled out the checkout information correctly,
# When I proceed through the checkout process,
# Then I should see the checkout overview page,
# And when I click the finish button,
# Then I should receive an order confirmation stating, "Thank you for your order!"

# User Story 4: Standard User Missing Postal Code Error
# As a standard user,
# I want to be prompted to enter all required checkout information,
# So that I can avoid checkout errors and successfully complete my purchase.
# Acceptance Criteria:

# Given I am logged in as "standard_user",
# And I have added items to my cart and navigated to the checkout page,
# When I enter my first name and last name but leave the postal code field blank,
# Then I should see an error message stating, "Error: postal code is required."