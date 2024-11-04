from data import *


## Task 1
#This function has one parameter (of type list[CountyDemographics]), a list of county demographics
# objects and must return the total 2014 Population across the set of counties in the provided list.
def population_total(lst: list[CountyDemographics]) -> int:
    sum = 0
    for i in lst:
        sum += i.population["2014 Population"]
    return sum

## Task 2
# This function has two parameters, a list of county demographics objects and a two-letter state
# abbreviation and must return a list of county demographics objects from the input list that are
# within the specified state.
def filter_by_state(lst: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    result = []
    for i in lst:
        if i.state == state:
            result.append(i)
    return result

## Task 3
#This function takes two parameters: a list of county demographics objects and the education key of interest
# (e.g., "Bachelor's Degree or Higher"). This function must return the total 2014 sub-population
# across the set of counties in the provided list for the specified key of interest.
def population_by_education(lst: list[CountyDemographics], key: str) -> float:
    pop = 0
    for i in lst:
        pop += (i.population["2014 Population"] * (i.education[key] / 100))
    return round(pop, 3)

# This function takes two parameters: a list of county demographics objects and the ethnicity key of interest and must return the total 2014
# sub-population across the set of counties in the provided list for the specified key of interest.
def population_by_ethnicity(lst: list[CountyDemographics], key: str) -> float:
    pop = 0
    for i in lst:
        if key not in i.ethnicities:
            return 0
        pop += (i.population["2014 Population"] * (i.ethnicities[key] / 100))
    return round(pop, 3)

#This function takes one parameter: a list of county demographics objects and must return the total 2014 sub-population indicated by income key
# 'Persons Below Poverty Level' across the set of counties in the provided list for the specified key of interest.
def population_below_poverty_level(lst: list[CountyDemographics]) -> float:
    pop = 0
    for i in lst:
        pop += (i.population["2014 Population"] * (i.income['Persons Below Poverty Level'] / 100))
    return round(pop, 3)

## Task 4
#This function takes two parameters: a list of county demographics objects and the education key of interest and must return the specified 2014 sub-population
# as a percentage of the total 2014 population across the set of counties in the provided list for the specified key of interest.
def percent_by_education(lst: list[CountyDemographics], key: str) -> float:
    #if key not in reduced_data:
        #return 0
    return round(population_by_education(lst, key) / population_total(lst), 3)
# This function takes two parameters: a list of county demographics objects and the ethnicity key of
# interest and must return the specified 2014 sub-population as a percentage of the total 2014
# population across the set of counties in the provided list for the specified key of interest.
def percent_by_ethnicity(lst: list[CountyDemographics], key: str) -> float:
    for i in lst:
        if key not in i.ethnicities:
            return 0
    return round(population_by_ethnicity(lst, key) / population_total(lst), 3)
# This functions takes one parameter: a list of county demographics objects and must return the
# 2014 sub-population indicated by income key 'Persons Below Poverty Level' as a percentage of the
# total 2014 population across the set of counties in the provided list for the specified key.
def percent_below_poverty_level(lst: list[CountyDemographics]) -> float:
    return round(population_below_poverty_level(lst) / population_total(lst), 3)

## Task 5
# Each takes three parameters: a list of county demographics objects, the education key of
# interest, and a numeric threshold value. This function must return a list of all county
# demographics objects for which the value for the specified key is greater than or less than
# (as appropriate by function name) the specified threshold value.
def education_greater_than(lst: list[CountyDemographics], key: str, thresh: float) -> list[CountyDemographics]:
    new = []
    for i in lst:
        if i.education[key] > thresh:
            new.append(i)
    return new

def education_less_than(lst: list[CountyDemographics], key: str, thresh:float) -> list[CountyDemographics]:
    new = []
    for i in lst:
        if i.education[key] < thresh:
            new.append(i)
    return new

def ethnicity_greater_than(lst: list[CountyDemographics], key: str, thresh: float) -> list[CountyDemographics]:
    new = []
    for i in lst:
        if i.ethnicities[key] > thresh:
            new.append(i)
    return new

def ethnicity_less_than(lst: list[CountyDemographics], key: str, thresh: float) -> list[CountyDemographics]:
    new = []
    for i in lst:
        if i.ethnicities[key] < thresh:
            new.append(i)
    return new

# Each takes two parameters: a list of county demographics objects and a numeric threshold value.
# and must return a list of all county demographics objects for which the value for key
# 'Persons Below Poverty Level' is greater than or less than (as appropriate by function name)
# the specified threshold value.
def below_poverty_level_greater_than(lst: list[CountyDemographics], thresh: float) -> list[CountyDemographics]:
    new = []
    for i in lst:
        if i.income['Persons Below Poverty Level'] > thresh:
            new.append(i)
    return new

def below_poverty_level_less_than(lst: list[CountyDemographics], thresh: float) -> list[CountyDemographics]:
    new = []
    for i in lst:
        if i.income['Persons Below Poverty Level'] < thresh:
            new.append(i)
    return new






