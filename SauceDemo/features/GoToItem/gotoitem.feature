Feature: Go to item page

    Scenario Outline: check whether user can go to item page and the info is correct
        Given User should login to swag labs using correct <username> and <password>
        When user clicks on the <item> link
        Then User should see the <item> page
        And User should see the <item> info is correct

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
