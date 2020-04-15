from urllib import request

def preprocess_raw_data(line):
    if '/' in line:
        return ''         
    line = line.replace(' ', ',',2)         
    return (line + '\n')

def loadVHI():
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2019&type=Mean"
    base_filename = r"vhi_"
    for i in range(1, 28):
        if i == 12 or i == 20:
            continue
        j = swap_id(i)
        print('{}{}{}'.format('loading vhi_', j, '.csv'))  
        local_url = url.format(str(i))
        response = request.urlopen(local_url) 
        csv = response.read() 
        csv_str = str(csv)     
        lines = csv_str.split("\\n")  
        with open(base_filename + str(j) + ".csv", "w") as fx: 
            fx.write("year,week,SMN,SMT,VCI,TCI,VHI\n") 
            for line in lines:
                fx.write(preprocess_raw_data(line))
                

def swap_id(i):
    my_dict = { 
    1:22,
    2:24,
    3:23,
    4:25,
    5:3,
    6:4,
    7:8,
    8:19,
    9:20,
    10:21,
    11:9,
    13:10,
    14:11,
    15:12,
    16:13,
    17:14,
    18:15,
    19:16,
    21:17,
    22:18,
    23:6,
    24:1,
    25:2,
    26:7,
    27:5
}
    return my_dict[i]





import pandas as pd
name='vhi_{}.csv'
frame = pd.DataFrame() 
for i in range(1, 26):
    temp = pd.read_csv(name.format(i), sep='[, ]+', engine='python')
    temp['Province'] = i
    frame = frame.append(temp, ignore_index=True)



def getByProvinceAndYear(province, year): 
    return frame[(frame['Province'] == province) & (frame['year'] == year)][['VHI', 'week', 'year']]

def getYearsInRestrictions(province, minVHI, maxVHI, procent):
    years = frame['year'].unique() 
    result = [] 
    for year in years:
        series = getByProvinceAndYear(province, year) 
        getMax = series[(series['VHI'] >= 60)]['VHI'].max()
        week = series[(series['VHI'] == getMax)]['week']
        count_in_range = series[(series['VHI'] >= minVHI) & (series['VHI'] <= maxVHI)]['VHI'].count() 
        procent_in_range = count_in_range * 100 / series['VHI'].count() 
        if procent_in_range >= procent: 
            result.append(week)
            result.append(year)
            
    return result