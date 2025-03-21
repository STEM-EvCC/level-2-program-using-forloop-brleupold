mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = len(mission_names)
sucessful_missions = 0
pre_2000 = []


for i in range(0,total_missions):
    if mission_success[i]==(True):
        sucessful_missions += 1

    if mission_years[i] < 2000:
        pre_2000.append(mission_names[i])


rate = (sucessful_missions / total_missions) * 100


print()
print(f"Total number of sucessful missions: {total_missions}")
print(f"Number of sucessful missions: {sucessful_missions}")
print(f"Success rate: {rate:.4}%")
print("Missions launched before the year 2000:")

for i in range(1,len(pre_2000)):
    print(f" -{pre_2000[i]}")

