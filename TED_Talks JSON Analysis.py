import json
with open("TED_Talks.json", "r") as file:
    TED_Talks_data=json.load(file)

# finds the number of talks in the dataset
len(TED_Talks_data)

# finds the headline, speaker and year_filmed of the talk with the highest number of views
# creates a list of each of the views
views_list = [(int(TED_Talks_data[talk]['views'])) for talk in range(len(TED_Talks_data))]
# finds the index of the max views in views_list
most_viewed_talk_index = (views_list.index(max(views_list)))
# then plugs that index back into TED_Talks_data to find other information
print([TED_Talks_data[most_viewed_talk_index][information] for information in ('headline','speaker','year_filmed',)])

# finds the mean number of views
mean_views = sum(views_list)//len(views_list)
print("the mean number of views is", mean_views)

# finds the median number of views
views_list.sort()
median_views = (views_list[len(views_list)//2] + views_list[len(views_list)//2+1])//2
print("the median number of views is", median_views)

# finds the percentage of talks that have more views than the mean or average number of views for a talk.
len([views for views in views_list if views > mean_views])*100/len(views_list)

# finds the headline of the talk that received the highest number of votes in the Confusing category.
# defines a function that returns the index for Confusing category within the 'rates' list for talk[j]
def list_index_of_Confusing_in_votes(j):
        return [i for i in range(0, 14) if TED_Talks_data[j]['rates'][i]['id'] == 2][0]
# appends the Confusing vote count for each talk to list_of_confusing_votes
list_of_Confusing_votes = []
for p in range(0, len(TED_Talks_data)):    
        list_of_Confusing_votes.append(TED_Talks_data[p]['rates'][list_index_of_Confusing_in_votes(p)]['count'])
most_Confusing_talk_index = (list_of_Confusing_votes.index(max(list_of_Confusing_votes)))
# prints the headline of the talk with the most Confusing votes by matching the index of the highest votes to its talk
print(TED_Talks_data[most_Confusing_talk_index]['headline'])

# Rest below is finding the headline and the year_filmed of the talk that received the highest percentage of votes in the Fascinating category.

# defines a function that returns the percentage of Fascinating votes for talk[j]
def percentage_of_fascinating_votes(j):
    # returns the index for Fascinating category within the 'rates' list for talk[j]
    index_of_fascinating_in_rates = [i for i in range(0, 14) if TED_Talks_data[j]['rates'][i]['id'] == 22][0]

    # for the talk[j], adds the number of votes for each category together 
    totalvotes = 0
    for l in range(0, 14):
        totalvotes += (TED_Talks_data[j]['rates'][l]['count'])
    
    # returns number of Fascinating votes times 100 divided by Total Votes for percentage
    return (TED_Talks_data[j]['rates'][index_of_fascinating_in_rates]['count']) * 100 / totalvotes

list_of_fascinating_percentages = []

# appends the Fascinating vote percentage for each talk to list_of_fascinating_percentages
for p in range(0, len(TED_Talks_data)):
    list_of_fascinating_percentages.append(percentage_of_fascinating_votes(p))

# finds the index of the most fascinating talk in list_of_fascinating_percentages:
most_fascinating_talk_index = (list_of_fascinating_percentages.index(max(list_of_fascinating_percentages)))

# then plugs that index back into TED_Talks_data to find other information
print([TED_Talks_data[most_fascinating_talk_index][information] for information in ('headline', 'year_filmed')])