latitude = float(input("enter your latitude: "))
longitude = float(input("enter your longitude: "))

k_st = 38.902649
lat_the_white_house = 38.897789 
long_the_white_house = -77.036562
lat_downing_hall = 38.921669
long_downing_hall =  -77.021361
lat_dupont_circle = 38.909760 
long_dupont_circle = -77.043479
lat_union_station = 38.897698
long_union_station =  -77.007200

if latitude > k_st:
  print("You are north of K st")
elif latitude < k_st:
  print("You are south of K st")
else:
  print("")

if latitude > lat_the_white_house:
  print("You are north of the White House")
elif latitude < lat_the_white_house:
  print("You are south of the White House")
else:
  print("")
if longitude > long_the_white_house:
  print("You are east of the White House")
elif longitude < long_the_white_house: 
  print("You are west of the White House")
else:
  print("")



if latitude > lat_downing_hall:
  print("You are north of Downing Hall")
elif latitude < lat_downing_hall:
  print("You are south of Downing Hall")
else:
  print("")
if longitude > long_downing_hall:
  print("You are east of Downing hall")
elif longitude < long_downing_hall: 
  print("You are west of Downing Hall")
else:
  print("")


if latitude > lat_dupont_circle:
  print("You are north of Dupont Circle")
elif latitude < lat_dupont_circle:
  print("You are south of Dupont Circle")
else:
  print("")
if longitude > long_dupont_circle:
  print("You are east of Dupont Circle")
elif longitude < long_downing_hall: 
  print("You are west of Dupont Circle")
else:
  print("")

if latitude > lat_union_station:
  print("You are north of Union Station")
elif latitude < lat_union_station:
  print("You are south of Union Station")
else:
  print("")
if longitude > long_union_station:
  print("You are east of Union Station")
elif longitude < long_union_station: 
  print("You are west of Union Station")
else:
  print("")
