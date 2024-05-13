Feature: Checkout Process

    Scenario Outline: Complete checkout successfully for different users
        Given "<user_type>" has logged in and added items to the cart
        When the user navigates to the cart and proceeds to checkout
        And the user enters valid billing and shipping information
        And the user confirms the order
        Then the checkout should be successful and a confirmation message is displayed

    Scenario Outline: Checkout fails due to invalid payment information
        Given "<user_type>" has logged in and added items to the cart
        When the user navigates to the cart and proceeds to checkout
        And the user enters invalid payment information
        And the user attempts to confirm the order
        Then the checkout should fail and an error message regarding invalid payment details is displayed

    Scenario Outline: Checkout interrupted and resumed for different users
        Given "<user_type>" has logged in and added items to the cart
        When the user begins the checkout process but navigates away to continue shopping
        And then returns to the checkout page
        Then the user should find their checkout state preserved
        And can complete the checkout process

        Examples:
            | user_type               |
            | standard_user           |
            | problem_user            |
            | performance_glitch_user |
            | error_user              |
