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
        Then User should see the cart icon with wrong number of items clicked
        And User clicks the cart icon
        When User clicks the checkout button
        And User enters checkout information with "<FirstName>", "<LastName>", "<ZipCode>"
        Then Last Name will be empty
        And User clicks the continue button
        Then User should see the checkout overview page
        When User clicks the finish button
        Then User will stay on the checkout overview page
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