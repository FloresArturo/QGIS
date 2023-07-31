'''
CREATE DICTIONARY:
Includes the break value and the hex color code.
Obtains data from a csv file containing hex color codes as columns and id as the first column.
'''
path_to_style = r"path\to\file.csv"
min = 13 # minimum value
max = 45 # max value
id = "name" # name of the row to create color codes for

# read style file
file = pd.read_csv(path_to_style_csv, index_col=0)

# locate property codes
df = file.loc[id]

# calculate breaks
breaks = len(df)-1
rang = max - min
interval = rang/breaks
break_lst = [min]
for _ in range(breaks):
  last_item = break_lst[-1]
  new_item = last_item+interval
  break_lst.append(round(new_item, 1))

# create dictionary
dic = {}
for i, v in enumerate(break_lst):
  dic[v]=df[i] # the break value (v) is equal to the color code at the i location of the list (df)

print(f'The dictionary for {property} is = {dic}')
