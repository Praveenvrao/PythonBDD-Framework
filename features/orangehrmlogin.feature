Feature: Orange hrm login
  Scenario: Login Orangehrm with valid creds
    Given Launch the Chrome browser
    When Open orangehrm homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must login and Dashboard should open

  Scenario Outline: Login Orangehrm with valid creds
    Given Launch the Chrome browser
    When Open orangehrm homepage
    And Enter username "<Username>" and password "<Password>"
    And Click on login button
    Then User must login and Dashboard should open

    Examples:
      | Username | Password |
      | Admin    | admin123 |
      | Admin23  | Admin123 |
      | Abdin    | adhde123 |
