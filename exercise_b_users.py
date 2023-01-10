users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

jonathans_twitter_handle = users["Jonathan"]["twitter"]
print(jonathans_twitter_handle)
# 2. Get Erik's hometown

eriks_hometown = users["Erik"]["home_town"]
print(eriks_hometown)
# 3. Get the list of Erik's lottery numbers

eriks_lotto_numbers = users["Erik"]["lottery_numbers"]
print(eriks_lotto_numbers)
# 4. Get the species of Avril's pet Monty

avrils_pet = users["Avril"]["pets"][0]["species"]
print(avrils_pet)

# 5. Get the smallest of Erik's lottery numbers

smallest_lotto_number = min(eriks_lotto_numbers)
print(smallest_lotto_number)

# 6. Return an list of Avril's lottery numbers that are even
even_numbers = []
avrils_lotto_numbers = users['Avril']["lottery_numbers"]
for number in avrils_lotto_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        

print(even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
eriks_lotto_numbers.append(7)
print(eriks_lotto_numbers)

# 8. Change Erik's hometown to Edinburgh
new_home_erik = users["Erik"]["home_town"] = 'Edinburgh'
print(new_home_erik)


# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({'Dog' : 'Fluffy'})
print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary

users["Taylor"] =  {
    "twitter": "taylor9",
    "lottery_numbers": [1,2,3,4,5,6,7],
    "home_town": "Glasgow",
    "pets": [
      {
        "name": "woody",
        "species": "dog"
      }
    ]
  }

print(users)
