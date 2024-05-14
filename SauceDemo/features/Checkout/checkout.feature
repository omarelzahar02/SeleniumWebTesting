Feature: Complete Checkout Process
    User Story 1: Successful Checkout Process
    As a user,
    I want to successfully complete the checkout process after adding items to my cart,
    So that I can finalize my purchase and receive confirmation.
    definition of done: The user can finalize the purchase and see the order confirmation.

    User Story 2: Problem User Checkout Failure
    As a problem user,
    I want to be informed of required fields I might have missed during checkout,
    So that I can understand why I can't proceed with the checkout.
    definition of done: The user should see an error message indicating the missing required field.

    User Story 3: Error User Checkout Success
    As an error user,
    I want to successfully complete my checkout despite potential system issues,
    So that I can finalize my orders like other users.
    definition of done: The user can finalize the purchase and see the order confirmation.

    User Story 4: Standard User Missing Postal Code Error
    As a standard user,
    I want to be prompted to enter all required checkout information,
    So that I can avoid checkout errors and successfully complete my purchase.
    definition of done: The user should see an error message indicating the missing postal code.
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