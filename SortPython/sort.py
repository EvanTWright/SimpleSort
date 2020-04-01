def sort_text():
	SortMe = list();
	file = open('Sort Me.txt');

	#reads from Sort Me.txt file and appends to list 
	for name in file:
    		SortMe.append(name);
	file.close();

	#sorts alphabetically then by length.
	SortMe.sort()
	SortMe.sort(key=len)

	#returns the list for testing purposes 
	return SortMe;	