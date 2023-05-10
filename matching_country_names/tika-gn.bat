rem	https://tika.apache.org/2.7.0/gettingstarted.html
M:
cd M:\DEV\A-MOSCATELLI-WIKI\matching_country_names
type GeoNames.htm | java -jar ..\tika-app-2.7.0.jar --text > geonames.tika.txt

