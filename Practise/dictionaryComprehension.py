# dictionary comprehension - create dictionary using an expression
#                            can replace for loops and certain lambda functions
# dictionary - {key : expression for (key,value) in iterable }
# dictionary - {key : expression for (key,value) in iterable if condition}
# dictionary - {key : expression (if/else) for (key,value) in iterable }
# dictionary - {key : function(value) for (key,value) in iterable }
# -------------------------------------------------------------------------------
cities_in_F = {"newyork": 32, "helsinki": 57, "italy": 100}
cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}
#            {key : expression for (key,value) in iterable } ,we are using round to get value in round figure and items to display dictionary
print(cities_in_C)
# -------------------------------------------------------------------------
# dictionary -{key : expression for (key,value) in iterable if condition}
cities = {"newyork": "sunny", "helsinki": "sunny", "italy": "cold"}
cities_list = {key: value for (key, value) in cities.items() if value == "sunny"}
#            {key : expression for (key,value) in iterable } ,we are using round to get value in round figure and items to display dictionary
print(cities_list)
# ----------------------------------------------------------------------
# dictionary -{key : expression (if/else) for (key,value) in iterable}
cities_new = {"newyork": 38, "helsinki": 54, "italy": 100, "chocago": 20}
cities_last = {key: ("hot" if value >= 38 else "cold") for (key, value) in cities_new.items()}
print(cities_last)


# ------------------------------------------------------------------
# dictionary -{key : function(value) for (key,value) in iterable} -when we have more conditions and we want to pass value through function
def check_temp(value):
    if value >= 23:
        return "warm"
    elif 23 >= value >= 45:
        return "hot"
    else:
        return "cold"


city = {"delhi": 56, "kolkatta": 34, "mumbai": 23}
cities_las = {key: check_temp(value) for (key, value) in city.items()}
print(cities_las)
