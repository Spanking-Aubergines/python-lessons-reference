# match-case statement(switch): an alternative to using many 'elif' statements
#                                 execute some code if a value matches a 'case'
#                                 benefits: cleaner and syntax is more readeable


# def day_of_week(day):
#     match day:
#         case 1:
#             return "sunday"
#         case 2:
#             return "monday"
#         case 3:
#             return "tuesday"
#         case 4:
#             return "wednesday"
#         case 5:
#             return "thursday"
#         case 6:
#             return "friday"
#         case 7:
#             return "saturday"
#         case _:
#             return "not a day"

# print (day_of_week(2))

def is_weekend(day):
    match day:
        case "saturday"|"sunday":
            return True
        case "monday" |"tuesday"|"wednesday"|"thursday"| "friday":
            return False
        case _:
            return "not a day"

print (is_weekend("sunday"))