import json
with open("movies.json", encoding="utf8") as file:
    movie_data=json.load(file)

class list_dict(list):
            
    def sort_by_dict_value(self, key_to_sort, ascending = True):
        movies_with_parameter = []        # creates a list that we'll fill with the movies that actually contain parameter
        for i in range(len(movie_data)):                       # iterates through all the movies
            if (movie_data[i][key_to_sort]) != None:           # if data for the specified key is present (!= None)
                movies_with_parameter.append(movie_data[i])    # then we'll add that movie's dictionary to our list
                def myFunc(e):
                    return e[key_to_sort]
                if ascending == False:                         # depending on specified order, will sort the list by our key
                    movies_with_parameter.sort(reverse=True, key=myFunc)
                elif ascending == True:
                    movies_with_parameter.sort(key=myFunc)
        return movies_with_parameter                # returns our list of dictionaries that has now been sorted to our needs

mov = list_dict(movie_data)

# the name of the 45th movie in the sorted list of dictionaries by production budget
production_budget_sorted = mov.sort_by_dict_value('Production Budget')
production_budget_sorted[44]['Title']

# the name of the 2nd movie in the sorted list of dictionaries by worldwide gross (descending)
production_budget_sorted = mov.sort_by_dict_value('Worldwide Gross', False)
production_budget_sorted[1]['Title']