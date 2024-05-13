Feature: Remove Items from Cart

    Scenario Outline: Successfully remove an item from the cart
        Given "<user_type>" has logged in and added multiple items to the cart
        When the user decides to remove an item from the cart
        Then the item should be successfully removed
        And the cart should reflect the updated item count

    Scenario Outline: Attempt to remove an item not in the cart
        Given "<user_type>" has logged in with an empty cart
        When the user attempts to remove an item that is not in the cart
        Then the system should display an error message indicating the item is not in the cart

    Scenario Outline: Remove all items from the cart
        Given "<user_type>" has logged in and filled the cart with items
        When the user removes all items from the cart one by one
        Then the cart should be empty
        And the user should see a message indicating the cart is empty

        Examples:
            | user_type               |
            | standard_user           |
            | problem_user            |
            | performance_glitch_user |
            | error_user              |
