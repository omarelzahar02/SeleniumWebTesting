Feature: Sorting items in the main page

    Scenario Outline: Check whether user can remove cart items from cart
        Given User should login to swag labs using correct <Username> and <Password>
        When User clicks sort doropdown
        And User selects <SortOption>
        Then User should see the items sorted by <SortOption>

    Examples:
        | Username      | Password     | SortOption            |
        | standard_user | secret_sauce | Name (A to Z)         |
        | standard_user | secret_sauce | Name (Z to A)         |
        | standard_user | secret_sauce | Price (low to high)   |
        | standard_user | secret_sauce | Price (high to low)   |

        | problem_user  | secret_sauce | Name (A to Z)         |
        | problem_user  | secret_sauce | Name (Z to A)         |
        | problem_user  | secret_sauce | Price (low to high)   |
        | problem_user  | secret_sauce | Price (high to low)   |

        | error_user    | secret_sauce | Name (A to Z)         |
        | error_user    | secret_sauce | Name (Z to A)         |
        | error_user    | secret_sauce | Price (low to high)   |
        | error_user    | secret_sauce | Price (high to low)   |

        | visual_user   | secret_sauce | Name (A to Z)         |
        | visual_user   | secret_sauce | Name (Z to A)         |
        | visual_user   | secret_sauce | Price (low to high)   |
        | visual_user   | secret_sauce | Price (high to low)   |