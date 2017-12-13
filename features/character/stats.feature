# Created by Tymoteusz Paul at 12/12/2017
Feature: Character stats
  Characters on TI are described by a lot of different statistics, affects,
  numbers and various states. It is important that those are correctly displayed
  and coherent across various display functions.

  Background: Setting scales
    Given "attack_defense" scales table
      | rank  | name            |
      | 1     | Pathetic        |
      | 2     | Below Average   |
      | 3     | Average         |
      | 4     | Above Average   |
      | 5     | Strong          |
      | 6     | Mighty          |
      | 7     | Peerless        |
      | 8     | Legendary       |
      | 9     | Godly           |
    And "health_level" scales table
      | rank  | name            |
      | 1     | Perfect         |
      | 2     | Excellent       |
      | 3     | Scratched       |
      | 4     | Bruised         |
      | 5     | Battered        |
      | 6     | Hurt            |
      | 7     | Wounded         |
      | 8     | Injured         |
      | 9     | Mauled          |
      | 10    | Mangled         |
      | 11    | Crippled        |
      | 12    | Dying           |

  Scenario: Combat command for healthy person
    Given a healthy character with no injuries
    When I invoke "combat" command
    Then my "SubHP" should be "Perfect"
    And my "Attack" should be in "attack_defense" scales table
    And my "Defense" should be in "attack_defense" scales table
