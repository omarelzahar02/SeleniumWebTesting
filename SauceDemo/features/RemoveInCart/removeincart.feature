Feature: Remove Items from Cart

    Scenario Outline: Check whether user can remove cart items from cart
        Given User should login to swag labs using correct "<Username>" and "<Password>"
        And User clicks the add to cart buttons
        And User clicks the cart icon
        When User clicks the remove buttons
        Then User should see the cart without the removed item

        Examples:
            | Username      | Password     |
            | standard_user | secret_sauce |
            | problem_user  | secret_sauce |
            | error_user    | secret_sauce |
            | visual_user   | secret_sauce |

    Scenario: Item button should reset after item removal
        Given User is logged in with "standard_user" and "secret_sauce"
        And User adds an item to the cart
        And User navigates to the cart
        When User removes the item from the cart
        And User returns to the item listing page
        Then The item button should show "Add to cart"