# USA's GDP per capita from 1960 to 2021 is given by the tuple T in the code cell below. The values are arranged in ascending order of the year, i.e., the first value is for 1960, the second value is for 1961, and so on.
T = (3007, 3067, 3244, 3375,3574, 3828, 4146, 4336, 4696, 5032,5234,5609,6094,6726,7226,7801,8592,9453,10565,11674,12575,13976,14434,15544,17121,18237,19071,20039,21417,22857,23889,24342,25419,26387,27695,28691,29968,31459,32854,34515,36330,37134,37998,39490,41725,44123,46302,48050,48570,47195,48651,50066,51784,53291,55124,56763,57867,59915,62805,65095,63028,69288)

# Use list comprehension to produce a list of the gaps between consecutive entries in T, i.e, the increase in GDP per capita with respect to the previous year.
# for each year, starting with 1961, subtracts the previous year's GDP from that year's GDP
gdp_gaps = [(T[year] - T[year-1]) for year in range(1,len(T))]
print(gdp_gaps)

# uses built-in max function to find max value from gdp_gaps
max(gdp_gaps)     
print("The maximum increase in GDP per capita is", max(gdp_gaps))

# list comp that makes a new list of the gaps that are > 1000
(len([gap for gap in gdp_gaps if gap > 1000])*100/len(gdp_gaps))
print("The percentage of gaps that have size greater than $1000:", (len([gap for gap in gdp_gaps if gap > 1000])*100/len(gdp_gaps)), "%")

# makes a new dictionary entry for each year, with corresponding value via index from gdp_gaps
D = {year+1960:gdp_gaps[year-1] for year in range(1,len(T))}
print(D)

# returns the key and value from D if the key's corresponding value is the same as the max value
[(year, gap) for year,gap in D.items() if D[year] == max(D.values())]