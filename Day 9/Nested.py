capitals={
    "Afghanistan":"Kabul",
    "Iran":"Tehran",
    "USA":"Washington DC"
}

# travel_log={
#     "France":["paris","lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"]
# }

# for cities in travel_log:
#     for city in travel_log[cities]:
#         if city=="lille":
#             print(city)
    
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log={
    "France":{
        "cities_visited":["paris","lille","Dijon"],
        "total_visited":12
        
        },
    "Germany":{
        "cities_visited":["berlin","munich","stuttgart"],
        "total_visited":12
    }
}

print(travel_log["Germany"]["cities_visited"][0])