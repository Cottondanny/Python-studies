name = "Danny Htet"

first_name = name[:5]
second_name = name[6:10] #these are called idex or indexing operators. It goes like [start:stop:step]
funky_name = name[0:10:2] #step is something that skips and shows the letters in between start and stop

print(funky_name)


google = "http://google.com"
youtube = "http://youtube.com"

web_name = slice(7,-4) #slice or slice operators 

print(google[web_name]) 
print(youtube[web_name]) #slice function takes out the middle of the website 
