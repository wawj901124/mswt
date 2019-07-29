# Created by Administrator at 2019/7/29
Feature: Calculation
  # Enter feature description here
  Input two number, then compare result

  Scenario: Do a simple add method
    # Enter steps here
    Given I have two number : 2 and 5
    When Do add method
    Then I get result : 7