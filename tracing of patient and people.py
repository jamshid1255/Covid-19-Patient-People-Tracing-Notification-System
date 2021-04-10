import pandas as pd
import folium
import gmplot

from collections import defaultdict
import datetime
from datetime import timedelta
import folium
from haversine import haversine
import matplotlib.pyplot as plt


dct1 = defaultdict(list)
dct2 = defaultdict(list)
dct3 = defaultdict(list)
dct4 = defaultdict(list)
dct5 = defaultdict(list)

dct_1 = defaultdict(list)
dct_2 = defaultdict(list)
dct_3 = defaultdict(list)
dct_4 = defaultdict(list)
dct_5 = defaultdict(list)

# apikey = '' # (your API key here)
df = pd.read_csv(r'Data\tomorrow.csv')
colr = pd.read_csv(r'Data\ral_standard2.csv')

df['longitude'] = df['longitude'].astype(float)
df_long=df['longitude']  #To select longitude data

df['latitude'] = df['latitude'].astype(float)
df_lat=df['latitude']  #To select latitude data
longitude=df_long
latitude=df_lat

df['userid'] = df['userid'].astype(int)
user_id=df['userid']  #To select userid
userId=user_id

#age reading
df['age'] = df['age'].astype(int)
user_age=df['age'] 
userAge=user_age

#gender reading
df['gender'] = df['gender'].astype(str)
df_gender=df['gender']
userGender = df_gender

#print(colr['English'][0])

#for k in userId:
#    print(userId[])
df['Dates'] = pd.to_datetime(df['check in time']).dt.date
dates = df['Dates']

df['Time'] = pd.to_datetime(df['check in time']).dt.time
time = df['Time']

noPatient = int(input('How many Patients in Data '))
noPatientdec = noPatient
    
year = int(input('Enter a year '))
month = int(input('Enter a month '))
day = int(input('Enter a day '))
day1 = int(input('How many days data '))
date1 = datetime.date(year, month, day)

lat_high_limit = float(input('Enter high latitude  '))
lat_low_limit = float(input('Enter low latitude  '))

long_high_limit = float(input('Enter high longitude  '))
long_low_limit = float(input('Enter low longitude  '))

date_to = datetime.date(year, month, day+day1)
gmap = gmplot.GoogleMapPlotter(lat_high_limit,long_low_limit, 5)
i=0
j=0
l=0
p=0
me=0
latitude_list = []
longitude_list = []
mydate = []
myid = []
mee=0
size=len(userId)-1
print('Data from '+str(date1)+' to '+str(date_to))
# Mark a hidden gem:
print('Patient ID         Dates          Lititude       Longitude       Time')
for z in range(day1):
    date1 = datetime.date(year, month, day+z)
    #print(date1)
    no_ofPatient=0
    for k in range(len(userId)):
        dct1['var_{}'.format(no_ofPatient)]
        dct2['var_{}'.format(no_ofPatient)]
        dct3['var_{}'.format(no_ofPatient)]
        dct4['var_{}'.format(no_ofPatient)]
        dct5['var_{}'.format(no_ofPatient)]
        while (userId[i]==k):
            if dates[i]==date1:
                if ((latitude[i] <= lat_high_limit) and (latitude[i]>=lat_low_limit) and (longitude[i]<=long_high_limit) and (longitude[i]>=long_low_limit)):
                    print(str(k) + '                  '+ str(dates[i])+ '     ' + str(latitude[i])+'        '+ str(longitude[i]) + '       ' + str(time[i]))
                    #gmap.marker(latitude[i],longitude[i], color='cornflowerblue',size=2)
                    rad_lats, rad_lons = zip(*[(latitude[i], longitude[i])])
                    gmap.scatter( rad_lats, rad_lons, '#FF0000',size = 2, marker = False )
                    
                    dct1['var_'+str(no_ofPatient)].append(latitude[i])
                    dct2['var_'+str(no_ofPatient)].append(longitude[i])
                    dct3['var_'+str(no_ofPatient)].append(time[i])
                    dct4['var_'+str(no_ofPatient)].append(userAge[i])
                    dct5['var_'+str(no_ofPatient)].append(userGender[i])
                    
            i+=1
            if i==size:
                break
        #gmap.plot(dct1['var_'+str(no_ofPatient)], dct2['var_'+str(no_ofPatient)],'red', edge_width = 2.5)
        j+=1
        no_ofPatient+=1  
    i=0
    mee+=1





noOfPatient=0
colorList=0
sizeofDictionary = len(dct1)
for k in range(sizeofDictionary):
    SizeofKeys = len(dct1['var_'+str(k)])
    if SizeofKeys>=1:
        for i in range(SizeofKeys):
            dct_1['var_{}'.format(noOfPatient)]
            dct_2['var_{}'.format(noOfPatient)]
            dct_3['var_{}'.format(noOfPatient)]
            dct_4['var_{}'.format(noOfPatient)]
            dct_5['var_{}'.format(noOfPatient)]
            dct_1['var_'+str(noOfPatient)].append(dct1['var_'+str(k)][i])
            dct_2['var_'+str(noOfPatient)].append(dct2['var_'+str(k)][i])
            dct_3['var_'+str(noOfPatient)].append(dct3['var_'+str(k)][i])
            dct_4['var_'+str(noOfPatient)].append(dct4['var_'+str(k)][i])
            dct_5['var_'+str(noOfPatient)].append(dct5['var_'+str(k)][i])
            gmap.marker(dct1['var_'+str(k)][i],dct2['var_'+str(k)][i], '#'+(colr['HEX'][colorList]),size=2)
        noOfPatient+=1
        
        gmap.plot(dct_1['var_'+str(colorList)], dct_2['var_'+str(colorList)],'#'+(colr['HEX'][colorList]), edge_width = 2.5)
        colorList+=1



del dct1
del dct2
del dct3
del dct4
del dct5
print('size dct_1 ' + str((dct_1['var_'+str(0)])))

print('size dct_2 ' + str((dct_2['var_'+str(0)])))

print('size dct_3 ' + str((dct_3['var_'+str(0)])))

print('size dct_4 ' + str((dct_4['var_'+str(0)])))

print('size dct_5 ' + str((dct_5['var_'+str(0)])))


speesdate = datetime.date(2010, 7, 14)
me=0

sizeofdic = len(dct_1)
no_of_patient=1
for i in range(sizeofdic):
    sizeofkey = len(dct_1['var_'+str(i)])
    if sizeofkey > 1:
        #print('Patient distance covered ' + str(ll))
        for k in range(sizeofkey-1):
            print('Patient ' + str(no_of_patient))
            print('Point 1 (' + str(dct_1['var_'+str(i)][k]) + ',' + str(dct_2['var_'+str(i)][k])+')')
            print('Point 2 (' + str(dct_1['var_'+str(i)][k+1]) + ',' + str(dct_2['var_'+str(i)][k+1])+')')
            
            start_time = dct_3['var_'+str(i)][k]
            print('Time at point 1 is ' + str(start_time))
            end_time = dct_3['var_'+str(i)][k+1]
            print('Time at point 2 is ' + str(end_time))
            date = datetime.date(1, 1, 1)
            datetime1 = datetime.datetime.combine(date, start_time)
            datetime2 = datetime.datetime.combine(date, end_time)
            time_elapsed = datetime2 - datetime1

            twopoint_time = round((time_elapsed.total_seconds()/3600.0),3)
            distance=round((haversine((dct_1['var_'+str(i)][k], dct_2['var_'+str(i)][k]),(dct_1['var_'+str(i)][k+1], dct_2['var_'+str(i)][k+1]), unit='km')),3)
            speed = round((distance/twopoint_time),3)
            print('Time spent between these two points ' + str(twopoint_time) + ' hr')
            print('Distance Covered is ' + str(distance) +' km')
            print('Speed ' + str(speed) + ' km/h (kph)')
            if speed > 9:
                print('In Vehicle ')
            else:
                print('In Walking ')        
            print('')
        no_of_patient+=1

t=0
tum = noPatient
kill = 0
print(dct_1)
sizeofdic = len(dct_1)
print(sizeofdic)
dona = sizeofdic - noPatient
no_of_users=1
for i in range(noPatient):
    for l in range(dona):
        sizePatient = len(dct_1['var_'+str(noPatientdec-1)])
        sizeUser = len(dct_1['var_'+str(i+noPatient+kill)])
        if sizePatient <= sizeUser:
            sizeofkey = sizePatient
        else:
            sizeofkey = sizeUser
        #print(dct_1['var_'+str(noPatientdec-1)])
        #print('Patient '+ str(sizePatient))
        #print('User '+ str(sizeUser))
        #print(dct_1['var_'+str(i+noPatient+kill)])
        #print('Loop '+ str(sizeofkey))
        t=0
      #  print(dct_1['var_'+str(i+dona)])
       # print(str(noPatient)+ 'hi' + str(sizeofkey))
        if sizeofkey > 1:
            #print('Patient distance covered ' + str(ll))
            for k in range(sizeofkey):
                if t==0:
                    patient_time1 = dct_3['var_'+str(noPatientdec-1)][k]
                    patient_time2 = dct_3['var_'+str(noPatientdec-1)][k+sizeofkey-1]
                    user_time1 = dct_3['var_'+str(noPatient)][k]
                    user_time2 = dct_3['var_'+str(noPatient)][k+sizeofkey-1]
                    #print('Patient time 1 '+ str(patient_time1) + ' time 2 ' + str(patient_time2))
                    #print('Person time 1 '+ str(user_time1) + ' time 2 ' + str(user_time2))
                    t+=1
                    
                    Person_time1 = datetime.datetime.combine(date, user_time1)
                    Person_time2 = datetime.datetime.combine(date, user_time2)
                    personTotal_time_elapsed = Person_time2 - Person_time1
                    personTotal_time_Seconds = round((personTotal_time_elapsed.total_seconds()),3)
                    print('total seconds ' + str(personTotal_time_Seconds))
                # print('User ' + str(no_of_patient))
                patient_time = dct_3['var_'+str(noPatientdec-1)][k]
                user_time = dct_3['var_'+str(noPatient)][k]
                user_age = dct_4['var_'+str(noPatient)][k]
                user_gender = dct_5['var_'+str(noPatient)][k]
                #print('age ' + str(dct_4['var_'+str(noPatient)][k]) + ' gender ' + str(dct_5['var_'+str(noPatient)][k]))
                
            # if patient_time == user_time:
                print('Time at point of patient ' + str(patient_time) + ' User ' + str(user_time))
                print('Patient '+ str(i+1) + ' ('  + str(dct_1['var_'+str(noPatientdec-1)][k]) + ',' + str(dct_2['var_'+str(noPatientdec-1)][k])+')')
                print('User ' + str(noPatient+1)+ ' Point ' +str(k+1) + '  ('  + str(dct_1['var_'+str(noPatient)][k]) + ',' + str(dct_2['var_'+str(noPatient)][k])+')')
                distance=round((haversine((dct_1['var_'+str(noPatientdec-1)][k], dct_2['var_'+str(noPatientdec-1)][k]),(dct_1['var_'+str(noPatient)][k], dct_2['var_'+str(noPatient)][k]), unit='m')),3)
                print('Distance from patient is ' + str(distance) +' m')
                if distance <= 2 and personTotal_time_Seconds >= 20 and user_age >= 50 :
                    point1 = [dct_1['var_'+str(noPatientdec-1)][k], dct_2['var_'+str(noPatientdec-1)][k]]
                    point2 = [dct_1['var_'+str(noPatient)][k], dct_2['var_'+str(noPatient)][k]]
                    x_values = [point1[0], point2[0]]
                    y_values = [point1[1], point2[1]]
                    gmap.plot(x_values, y_values,'black')
                    gmap.text(dct_1['var_'+str(noPatient)][k],dct_2['var_'+str(noPatient)][k],'Distance ' +str(distance) + 'm, age '+ str(user_age) + ' High Probability of infection,Person is above 50 year age')
                elif distance <= 2 and personTotal_time_Seconds >= 20 and (user_age < 50 and user_age >=30):
                    point1 = [dct_1['var_'+str(noPatientdec-1)][k], dct_2['var_'+str(noPatientdec-1)][k]]
                    point2 = [dct_1['var_'+str(noPatient)][k], dct_2['var_'+str(noPatient)][k]]
                    x_values = [point1[0], point2[0]]
                    y_values = [point1[1], point2[1]]
                    gmap.plot(x_values, y_values,'black')
                    gmap.text(dct_1['var_'+str(noPatient)][k],dct_2['var_'+str(noPatient)][k],'Distance ' +str(distance) + 'm, age '+ str(user_age) + ' High Probability of infection,Person is in between 30 and 50 year age')
                elif distance <= 2 and personTotal_time_Seconds >= 20 and (user_age < 30 and user_age >=10):
                    point1 = [dct_1['var_'+str(noPatientdec-1)][k], dct_2['var_'+str(noPatientdec-1)][k]]
                    point2 = [dct_1['var_'+str(noPatient)][k], dct_2['var_'+str(noPatient)][k]]
                    x_values = [point1[0], point2[0]]
                    y_values = [point1[1], point2[1]]
                    gmap.plot(x_values, y_values,'black')
                    gmap.text(dct_1['var_'+str(noPatient)][k],dct_2['var_'+str(noPatient)][k],'Distance ' +str(distance) + 'm, age '+ str(user_age) + ' High Probability of infection,Person is in between 10 and 30 year age')
                #elif noPatientdec == 1:
                #    point1 = [dct_1['var_'+str(noPatientdec-1)][k], dct_2['var_'+str(noPatientdec-1)][k]]
                #    point2 = [dct_1['var_'+str(noPatient)][k], dct_2['var_'+str(noPatient)][k]]
                #    x_values = [point1[0], point2[0]]
                #    y_values = [point1[1], point2[1]]
                #    gmap.text(dct_1['var_'+str(noPatient)][k],dct_2['var_'+str(noPatient)][k],str(distance) + 'm ' + 'Low Probability of infection')
                    
            no_of_users+=1
            noPatient+=1
    noPatientdec-=1
    noPatient = tum
    kill-=1
    #print('Hi its mee' + str(noPatientdec))


gmap.draw('Output\patient_map.html')
