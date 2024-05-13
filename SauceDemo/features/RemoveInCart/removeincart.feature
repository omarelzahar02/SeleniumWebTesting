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

# User Story 1: Remove Items from Cart
# As a user,
# I want to be able to remove items from my shopping cart,
# So that I can adjust my final order before checkout.

# Acceptance Criteria:
# Given I am logged into SauceDemo with a valid username (e.g., standard_user, problem_user, error_user, visual_user) and password,
# And I have added items to my cart,
# When I view my cart and click the remove button for an item,
# Then I should no longer see that item in my cart.

# User Story 2: Reset Item Button After Removal
# As a user,
# I want the item button to reset to "Add to Cart" after I remove an item from my cart,
# So that I can easily add it back if I change my mind.

# Acceptance Criteria:

# Given I am logged into SauceDemo as "standard_user" using the correct password,
# And I have added an item to my cart,
# When I remove this item from my cart,
# And I return to the item listing page,
# Then the button for this item should display "Add to Cart," indicating that I can add it again.