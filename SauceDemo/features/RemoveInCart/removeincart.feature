Feature: Remove Items from Cart
    User Story 1: Remove Items from Cart
    As a user,
    I want to be able to remove items from my shopping cart,
    So that I can adjust my final order before checkout.
    definition of done: User should be able to remove items from the cart.

    User Story 2: Reset Item Button After Removal
    As a user,
    I want the item button to reset to "Add to Cart" after I remove an item from my cart,
    So that I can easily add it back if I change my mind.
    definition of done: The item button should show "Add to cart" after item removal.
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