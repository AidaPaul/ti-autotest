# Created by Tymoteusz Paul at 10/12/2017
Feature: Chargen
  Chargen is our newbie staging area and it's important to ensure that it has
  all the features we expect it to have and they are working correct, as trying
  patience of newbie players is a good way of losing them.

  Scenario Outline: Creating new items
    Given that we are in The Finishing Touches
    And we have empty inventory
    When we request "<item>"
    Then in inventory we should have "<string>"

    Examples: Clothes
      | item      | string                                                      |
      | hat       | a Lithmorran style men's hat, fashioned from a linen fabric |
      | bag       | a thick, coarse linen satchel, fit with wide leather straps |
      | pendant   | a small wooden chalice pendant hung from a strip of leather |
      | bracelet  | a knotted leather cord strung with multiple dangling charms |
      | belt      | a practical, leather belt hung with a functional coin purse |
      | sleeves   | loose linen sleeves with cuffs that extend past the fingers |
      | gloves    | a proper set of linen gloves, buttoning closed at the wrist |
      | tunic     | a loose fitting, collared linen tunic, laced along the neck |
      | cloak     | a voluminous cloak of soft woven fabric made without a hood |
      | hose      | a practically designed, fitted pair of masculine linen hose |
      | shoes     | a pair of comfortable hard leather shoes with a strong sole |

    Examples: Misc
      | item      | string                                                      |
      | mtatt     | a medium tattoo                                             |
      | statt     | a small tattoo                                              |
      | ltatt     | a large tattoo                                              |
