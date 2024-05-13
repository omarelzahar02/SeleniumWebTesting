Feature: add item to cart

    Scenario Outline: Check whether user can add items to cart the homepage
        Given User should login to swag labs using correct <username> and <password>
        When User adds <item> to cart
        Then User should see <item> in from cart

        Examples:
            | username      | password     | item                             |
            | standard_user | secret_sauce | Sauce Labs Backpack              |
            | standard_user | secret_sauce | Sauce Labs Bike Light            |
            | standard_user | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | standard_user | secret_sauce | Sauce Labs Fleece Jacket         |
            | standard_user | secret_sauce | Sauce Labs Onesie                |
            | standard_user | secret_sauce | Test.allTheThings() T-Shirt (Red)|

            | problem_user  | secret_sauce | Sauce Labs Backpack              |
            | problem_user  | secret_sauce | Sauce Labs Bike Light            |
            | problem_user  | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | problem_user  | secret_sauce | Sauce Labs Fleece Jacket         |
            | problem_user  | secret_sauce | Sauce Labs Onesie                |
            | problem_user  | secret_sauce | Test.allTheThings() T-Shirt (Red)|

            | error_user    | secret_sauce | Sauce Labs Backpack              |
            | error_user    | secret_sauce | Sauce Labs Bike Light            |
            | error_user    | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | error_user    | secret_sauce | Sauce Labs Fleece Jacket         |
            | error_user    | secret_sauce | Sauce Labs Onesie                |
            | error_user    | secret_sauce | Test.allTheThings() T-Shirt (Red)|

            | visual_user   | secret_sauce | Sauce Labs Backpack              |
            | visual_user   | secret_sauce | Sauce Labs Bike Light            |
            | visual_user   | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | visual_user   | secret_sauce | Sauce Labs Fleece Jacket         |
            | visual_user   | secret_sauce | Sauce Labs Onesie                |
            | visual_user   | secret_sauce | Test.allTheThings() T-Shirt (Red)|

    
    Scenario Outline: Check whether user can remove cart items from cart Item page
        Given User should login to swag labs using correct <username> and <password>
        And User opens the <item> page
        When User adds <item> to cart
        Then User should see <item> in from cart


        Examples:
            | username      | password     | item                             |
            | standard_user | secret_sauce | Sauce Labs Backpack              |
            | standard_user | secret_sauce | Sauce Labs Bike Light            |
            | standard_user | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | standard_user | secret_sauce | Sauce Labs Fleece Jacket         |
            | standard_user | secret_sauce | Sauce Labs Onesie                |
            | standard_user | secret_sauce | Test.allTheThings() T-Shirt (Red)|

            | problem_user  | secret_sauce | Sauce Labs Backpack              |
            | problem_user  | secret_sauce | Sauce Labs Bike Light            |
            | problem_user  | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | problem_user  | secret_sauce | Sauce Labs Fleece Jacket         |
            | problem_user  | secret_sauce | Sauce Labs Onesie                |
            | problem_user  | secret_sauce | Test.allTheThings() T-Shirt (Red)|

            | error_user    | secret_sauce | Sauce Labs Backpack              |
            | error_user    | secret_sauce | Sauce Labs Bike Light            |
            | error_user    | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | error_user    | secret_sauce | Sauce Labs Fleece Jacket         |
            | error_user    | secret_sauce | Sauce Labs Onesie                |
            | error_user    | secret_sauce | Test.allTheThings() T-Shirt (Red)|

            | visual_user   | secret_sauce | Sauce Labs Backpack              |
            | visual_user   | secret_sauce | Sauce Labs Bike Light            |
            | visual_user   | secret_sauce | Sauce Labs Bolt T-Shirt          |
            | visual_user   | secret_sauce | Sauce Labs Fleece Jacket         |
            | visual_user   | secret_sauce | Sauce Labs Onesie                |
            | visual_user   | secret_sauce | Test.allTheThings() T-Shirt (Red)|
