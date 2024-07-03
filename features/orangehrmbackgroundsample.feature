Feature: OrangeHRM
  Background: common steps
    Given Launch the Chrome browser
    When Open orangehrm homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button

  Scenario: Verify login and Dashboard
    Then User must login and Dashboard should open

  Scenario: Login and check search page
    Then Navigate to search page and check

  Scenario:
    When Navigate to Directory
    Then User should land on Directory