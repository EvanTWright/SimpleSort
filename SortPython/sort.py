SortMe = list();
file = open('Sort Me.txt');


for name in file:
    SortMe.append(name);
file.close();

#sorts alphabetically then by length.
SortMe.sort();
SortMe.sort(key=len);

for name in SortMe:
    print(name)
