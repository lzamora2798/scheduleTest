
def processOverlap(range_1,range_2):
    return (range_1[0]<= range_2[1]) and (range_2[0]<range_1[1])

def convertToSeconds(time):
    hour,minutes = time.strip().split(":")
    hour_seconds = int(hour) * 3600
    minutes_seconds = int(minutes) * 60 
    return hour_seconds + minutes_seconds

def processFile(file):
    schedules_dic ={}
    names_dic = {}
    names_list = []

    try:
    #build the main dic
        for row in file:
            name,schedules = row.strip().split("=")
            schedules = schedules.split(",")
            for schedule in schedules:
                day = schedule[:2]
                time_range = schedule[2:].split("-")
                schedules_dic[day] = schedules_dic.get(day,{})
                schedules_dic[day][name] = [convertToSeconds(i) for i in time_range] 
            names_list.append(name)
        
        #proccess the dic 
        
        for value in schedules_dic.values():
            if len(value)>1:
                data_list = list(value.items())
                for idx,(name_1,range_1) in enumerate(data_list):
                    for name_2,range_2 in data_list[idx + 1:]:
                        if processOverlap(range_1,range_2):
                            names_dic[(name_1,name_2)] = names_dic.get((name_1,name_2),0) +1

        return names_dic
    except Exception as ex:
        return None


