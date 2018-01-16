# Created by Tymoteusz Paul at 08/01/2018
Feature: RPXP reset bug
  There is a bug which causes the RPXP counter to resert in certain situations
  and it's quite annoying to repeat and subsequently debug, hence tests to
  capture it automatically.

  Scenario: Two players in neutral room
    Given there are two players in a room with no action set
    And "first player" RPxp is "Low"
    When "first player" thinks "Some test thought"
    And "first player" sets an action "test action"
    Then "first player" RPxp is "Fair"
