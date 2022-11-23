import re
import urllib.request
#https://www.weather-forecast.com/locations/Cairo/forecasts/latest
city= input("enter yout city:")
url= "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data=urllib.request.urlopen(url).read()
data1= data.decode("utf-8")
print(data1)
m= re.search('span class="phrase">',data1)
start=m.end()
end= start+300
newstring=data1[start:end]
print(newstring)

m=re.search("</span>",newstring)
end=m.start()-2
final= newstring[0:end]
print(final)
