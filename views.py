from collections import Counter
from datetime import datetime

import numpy as np
import pandas as pd
from django.shortcuts import render, redirect

from .form import Forms

df = pd.read_csv('/Users/macosx/Desktop/DRONE/interessant/VEHICULE_USERS.csv', sep=r'\s*,\s*', header=0,
                 encoding='ascii', engine='python')

df.columns = df.columns.str.strip()

ufo_cols = ['DATE', 'ENT/PER ', 'DRONE/VEH', 'PASSAGERS', 'FREQUENE', 'DEPART ', 'ARRIVE ', 'POIDS', 'DISTANCE',
            'FRAGILE', 'DANGEREUX', 'OBJECT', 'CONTRAT', 'PRIX']

df1 = pd.read_csv('/Users/macosx/Desktop/DRONE/interessant/DRONE_Data1.csv', names=ufo_cols, sep=',', header=0,
                  error_bad_lines=False)

df1.columns = df1.columns.str.strip()

df2 = pd.read_csv('/Users/macosx/Desktop/DRONE/interessant/capteurs_drone1.csv')
df2.columns = df2.columns.str.strip()

df3 = pd.read_csv('/Users/macosx/Desktop/DRONE/green_vehicles1.csv')
def dash(country, col):
    df_FRANCE = df.loc[lambda x: x['Country'] == country]

    dict1 = Counter(df_FRANCE[col])
    values_list = []
    count_list = []
    counts_list = []
    for key in dict1.keys():
        values_list.append(key)

    for value in dict1.values():
        counts_list.append(value)
    for i in counts_list:
        S = (i / sum(counts_list)) * 100
        count_list.append(S)

    return (values_list, count_list)


# longitude latitude
import os

os.listdir()
import geopy

dir(geopy)
from geopy.geocoders import Nominatim

nom = Nominatim(user_agent='dounia.driff@gmail.com')

depart_latitude = []
depart_longitude = []
for adresse in df1['DEPART']:
    try:
        n = nom.geocode(adresse)
        depart_latitude.append(n.latitude)
        depart_longitude.append(n.longitude)


    except:
        None

df1['cordinate_depart'] = df1['DEPART'].apply(nom.geocode)

df1['depart_latitude'] = df1['cordinate_depart'].apply(lambda x: x.latitude if x != None else None)
df1['depart_longitude'] = df1['cordinate_depart'].apply(lambda x: x.longitude if x != None else None)

df1['cordinate_arrive'] = df1['ARRIVE'].apply(nom.geocode)
df1['arrive_latitude'] = df1['cordinate_arrive'].apply(lambda x: x.latitude if x != None else None)
df1['arrive_longitude'] = df1['cordinate_arrive'].apply(lambda x: x.longitude if x != None else None)


# lon lat


def haversine(lat1, lon1, lat2, lon2, to_radians=True, earth_radius=6371):
    if to_radians:
        lat1, lon1, lat2, lon2 = np.radians([lat1, lon1, lat2, lon2])

    a = np.sin((lat2 - lat1) / 2.0) ** 2 + \
        np.cos(lat1) * np.cos(lat2) * np.sin((lon2 - lon1) / 2.0) ** 2

    return earth_radius * 2 * np.arcsin(np.sqrt(a))


df1['dist'] = haversine(df1.depart_latitude.shift(), df1.depart_longitude.shift(),
                        df1.arrive_latitude.shift(), df1.arrive_longitude.shift())


def hi(request):
    varA = pd.unique(df['Engine']).tolist()
    total0 = df['Engine'].value_counts().sum()
    countt = (df['Engine'].value_counts() / total0 * 100).tolist()

    var_trusted = pd.unique(df['trusted_bland']).tolist()
    total1 = df['trusted_bland'].value_counts().sum()
    count_trusted = (df['trusted_bland'].value_counts() / total1 * 100).tolist()

    var_safe = pd.unique(df['safety']).tolist()
    total2 = df['safety'].value_counts().sum()
    count_safe = (df['safety'].value_counts() / total2 * 100).tolist()

    var_company = pd.unique(df['company']).tolist()
    total3 = df['company'].value_counts().sum()
    count_company = (df['company'].value_counts() / total3 * 100).tolist()

    buying_list = df['Buying'].value_counts().sort_values(ascending=False).index.tolist()
    buying = pd.unique(buying_list).tolist()

    B1 = buying[0]
    B2 = buying[1]
    B3 = buying[2]

    # Filter data to FRANCE

    today = datetime.now().ctime()
    context = {"countt": countt, "varA": varA, "today": today, "var_trusted": var_trusted,
               "count_trusted": count_trusted, "var_safe": var_safe, "count_safe": count_safe,
               "var_company": var_company, "count_company": count_company, "B1": B1, "B2": B2, "B3": B3,

               }

    return render(request, 'intellapp/index.html', context)


# Create your views here.


def hi1(request):
    A = 'FRANCE'
    df_FRANCE = df.loc[lambda x: x['Country'] == 'FRANCE']

    GvarA = dash('FRANCE', 'Engine')[0]
    Gcountt = dash('FRANCE', 'Engine')[1]

    Gvar_trusted = dash('FRANCE', 'trusted_bland')[0]
    Gcount_trusted = dash('FRANCE', 'trusted_bland')[1]

    Gvar_safe = dash('FRANCE', 'safety')[0]
    Gcount_safe = dash('FRANCE', 'safety')[1]

    Gvar_company = dash('FRANCE', 'company')[0]
    Gcount_company = dash('FRANCE', 'company')[1]

    buying_list = df_FRANCE['Buying'].value_counts().sort_values(ascending=False).index.tolist()
    Fbuying = pd.unique(buying_list).tolist()

    GB1 = Fbuying[0]
    GB2 = Fbuying[1]
    GB3 = Fbuying[2]

    today = datetime.now().ctime()
    context = {
        "Gcountt": Gcountt, "GvarA": GvarA, "Gvar_trusted": Gvar_trusted, "today": today,
        "Gcount_trusted": Gcount_trusted, "Gvar_safe": Gvar_safe, "Gcount_safe": Gcount_safe,
        "Gvar_company": Gvar_company, "Gcount_company": Gcount_company, "GB1": GB1, "GB2": GB2, "GB3": GB3
    }

    return render(request, 'intellapp/FRANCE.html', context)


# Create your views here.
def hi2(request):
    # Filter data to FRANCE
    A = 'GERMANY'
    df_FRANCE = df.loc[lambda x: x['Country'] == A]

    GvarA = dash(A, 'Engine')[0]
    Gcountt = dash(A, 'Engine')[1]

    Gvar_trusted = dash(A, 'trusted_bland')[0]
    Gcount_trusted = dash(A, 'trusted_bland')[1]

    Gvar_safe = dash(A, 'safety')[0]
    Gcount_safe = dash(A, 'safety')[1]

    Gvar_company = dash(A, 'company')[0]
    Gcount_company = dash(A, 'company')[1]

    buying_list = df_FRANCE['Buying'].value_counts().sort_values(ascending=False).index.tolist()
    Fbuying = pd.unique(buying_list).tolist()

    GB1 = Fbuying[0]
    GB2 = Fbuying[1]
    GB3 = Fbuying[2]

    today = datetime.now().ctime()
    context = {
        "Gcountt": Gcountt, "GvarA": GvarA, "Gvar_trusted": Gvar_trusted, "today": today,
        "Gcount_trusted": Gcount_trusted, "Gvar_safe": Gvar_safe, "Gcount_safe": Gcount_safe,
        "Gvar_company": Gvar_company, "Gcount_company": Gcount_company, "GB1": GB1, "GB2": GB2, "GB3": GB3
    }

    return render(request, 'intellapp/GERMANY.html', context)


# Create your views here.
def hi3(request):
    # Filter data to FRANCE
    A = 'CANADA'
    df_FRANCE = df.loc[lambda x: x['Country'] == A]

    GvarA = dash(A, 'Engine')[0]
    Gcountt = dash(A, 'Engine')[1]

    Gvar_trusted = dash(A, 'trusted_bland')[0]
    Gcount_trusted = dash(A, 'trusted_bland')[1]

    Gvar_safe = dash(A, 'safety')[0]
    Gcount_safe = dash(A, 'safety')[1]

    Gvar_company = dash(A, 'company')[0]
    Gcount_company = dash(A, 'company')[1]

    buying_list = df_FRANCE['Buying'].value_counts().sort_values(ascending=False).index.tolist()
    Fbuying = pd.unique(buying_list).tolist()

    GB1 = Fbuying[0]
    GB2 = Fbuying[1]
    GB3 = Fbuying[2]

    today = datetime.now().ctime()
    context = {
        "Gcountt": Gcountt, "GvarA": GvarA, "Gvar_trusted": Gvar_trusted, "today": today,
        "Gcount_trusted": Gcount_trusted, "Gvar_safe": Gvar_safe, "Gcount_safe": Gcount_safe,
        "Gvar_company": Gvar_company, "Gcount_company": Gcount_company, "GB1": GB1, "GB2": GB2, "GB3": GB3
    }

    return render(request, 'intellapp/CANADA.html', context)


# Create your views here.
def hi4(request):
    # Filter data to FRANCE
    A = 'UNITED KINDOM'
    df_FRANCE = df.loc[lambda x: x['Country'] == A]

    GvarA = dash(A, 'Engine')[0]
    Gcountt = dash(A, 'Engine')[1]

    Gvar_trusted = dash(A, 'trusted_bland')[0]
    Gcount_trusted = dash(A, 'trusted_bland')[1]

    Gvar_safe = dash(A, 'safety')[0]
    Gcount_safe = dash(A, 'safety')[1]

    Gvar_company = dash(A, 'company')[0]
    Gcount_company = dash(A, 'company')[1]

    buying_list = df_FRANCE['Buying'].value_counts().sort_values(ascending=False).index.tolist()
    Fbuying = pd.unique(buying_list).tolist()

    GB1 = Fbuying[0]
    GB2 = Fbuying[1]
    GB3 = Fbuying[2]

    today = datetime.now().ctime()
    context = {
        "Gcountt": Gcountt, "GvarA": GvarA, "Gvar_trusted": Gvar_trusted, "today": today,
        "Gcount_trusted": Gcount_trusted, "Gvar_safe": Gvar_safe, "Gcount_safe": Gcount_safe,
        "Gvar_company": Gvar_company, "Gcount_company": Gcount_company, "GB1": GB1, "GB2": GB2, "GB3": GB3
    }
    return render(request, 'intellapp/UK.html', context)


# Create your views here.
def hi5(request):
    # Filter data to FRANCE
    A = 'UNITED STATES'
    df_FRANCE = df.loc[lambda x: x['Country'] == A]

    GvarA = dash(A, 'Engine')[0]
    Gcountt = dash(A, 'Engine')[1]

    Gvar_trusted = dash(A, 'trusted_bland')[0]
    Gcount_trusted = dash(A, 'trusted_bland')[1]

    Gvar_safe = dash(A, 'safety')[0]
    Gcount_safe = dash(A, 'safety')[1]

    Gvar_company = dash(A, 'company')[0]
    Gcount_company = dash(A, 'company')[1]

    buying_list = df_FRANCE['Buying'].value_counts().sort_values(ascending=False).index.tolist()
    Fbuying = pd.unique(buying_list).tolist()

    GB1 = Fbuying[0]
    GB2 = Fbuying[1]
    GB3 = Fbuying[2]

    today = datetime.now().ctime()
    context = {
        "Gcountt": Gcountt, "GvarA": GvarA, "Gvar_trusted": Gvar_trusted, "today": today,
        "Gcount_trusted": Gcount_trusted, "Gvar_safe": Gvar_safe, "Gcount_safe": Gcount_safe,
        "Gvar_company": Gvar_company, "Gcount_company": Gcount_company, "GB1": GB1, "GB2": GB2, "GB3": GB3
    }
    return render(request, 'intellapp/USA.html', context)


# Create your views heremyChart.
def hi6(request):
    today = datetime.now().ctime()
    import pandas as pd

    # df1 = pd.read_csv('/Users/macosx/Desktop/DRONE/interessant/DRONE_Data.csv')
    # ufo_cols = ['DATE', 'ENT/PER ', 'DRONE/VEH', 'PASSAGERS', 'FREQUENE', 'DEPART ', 'ARRIVE ', 'POIDS', 'DISTANCE',
    #            'FRAGILE', 'DANGEREUX', 'OBJECT', 'CONTRAT', 'PRIX']
    # df1.columns = ufo_cols
    # df1.columns = ufo_cols

    # df1 = pd.read_csv('/Users/macosx/Desktop/DRONE/interessant/DRONE_Data.csv', names=ufo_cols, header=0)
    # df1 = pd.read_csv('/Users/macosx/Desktop/DRONE/interessant/VEHICULE_DATA_NEW.csv')

    # mean passagers
    df_DRONE = df1.loc[lambda x: x['DRONE/VEH'] == 'DRONE AUTONOME']

    df1['price'] = df1['PRIX'].apply(lambda x: x / df1['dist'] if (x > 50) else x)

    mean_passagers = int(df_DRONE['PASSAGERS'].mean())
    mean_poids = int(df_DRONE['POIDS'].mean())
    mean_freqence = int(df_DRONE['FREQUENE'].mean())

    df_DRONE = df1.loc[lambda x: x['DRONE/VEH'] == 'DRONE AUTONOME']
    mean_distance = df_DRONE['dist'].mean()
    mean_distance_km = mean_distance * 0.001

    list_fragile = pd.unique(df_DRONE['FRAGILE']).tolist()
    total = df_DRONE['FRAGILE'].value_counts().sum()
    pour_fragile = (df_DRONE['FRAGILE'].value_counts() / total * 100).tolist()
    pourc_fragile = pour_fragile[1]

    list_dangereux = pd.unique(df_DRONE['DANGEREUX']).tolist()
    total2 = df_DRONE['DANGEREUX'].value_counts().sum()
    pour_dangereux = (df_DRONE['DANGEREUX'].value_counts() / total2 * 100).tolist()
    pourc_dangereux = pour_dangereux[1]

    list_contrat = pd.unique(df_DRONE['CONTRAT']).tolist()

    total3 = df_DRONE['CONTRAT'].value_counts().sum()
    pour_contrat = (df_DRONE['CONTRAT'].value_counts() / total3 * 100).tolist()
    pourc_contrat = pour_contrat[1]

    prix_list = df_DRONE['PRIX'].tolist()

    # prix_list = df_DRONE['price'].dropna().tolist()

    df_DRONE = df1.loc[lambda x: x['DRONE/VEH'] == 'DRONE AUTONOME']
    df_per = df_DRONE.loc[lambda x: x['ENT/PER'] == 'Personne']
    df_ent = df_DRONE.loc[lambda x: x['ENT/PER'] == 'Entreprise']
    L = [(len(df_per.index) * 100) / len(df_DRONE)]
    L1 = [(len(df_ent.index) * 100) / len(df_DRONE)]

    leni = len(df_DRONE)

    context = {"mean_passagers": mean_passagers, "mean_poids": mean_poids, "mean_freqence": mean_freqence,
               "today": today, "mean_distance": mean_distance, "pour_fragile": pour_fragile,
               "pour_dangereux": pour_dangereux, "pour_contrat": pour_contrat,
               "list_fragile": list_fragile, "list_dangereux": list_dangereux, "list_contrat": list_contrat,
               "pourc_contrat": pourc_contrat,
               "pourc_fragile": pourc_fragile, "pourc_dangereux": pourc_dangereux, " leni": leni,
               "mean_distance_km": mean_distance_km, "prix_list": prix_list, "L": L, "L1": L1}
    return render(request, 'intellapp/MAROC.html', context)


# Create your views heremyChart.
def hi9(request):
    today = datetime.now().ctime()

    import pandas as pd

    # df1 = pd.read_csv('/Users/macosx/Desktop/DRONE/interessant/VEHICULE_DATA_NEW.csv')
    # mean passagers
    df_DRONE = df1.loc[lambda x: x['DRONE/VEH'] == 'VÉHÉCULE ÉLÉCTRIQUE AUTONOME']

    mean_passagers = int(df_DRONE['PASSAGERS'].mean())
    mean_poids = int(df_DRONE['POIDS'].mean())
    mean_freqence = int(df_DRONE['FREQUENE'].mean())

    df_DRONE = df1.loc[lambda x: x['DRONE/VEH'] == 'VÉHÉCULE ÉLÉCTRIQUE AUTONOME']
    mean_distance = df_DRONE['dist'].mean()
    mean_distance_km = mean_distance * 0.001

    list_fragile = pd.unique(df_DRONE['FRAGILE']).tolist()
    total = df_DRONE['FRAGILE'].value_counts().sum()
    pour_fragile = (df_DRONE['FRAGILE'].value_counts() / total * 100).tolist()
    pourc_fragile = pour_fragile[1]

    list_dangereux = pd.unique(df_DRONE['DANGEREUX']).tolist()
    total2 = df_DRONE['DANGEREUX'].value_counts().sum()
    pour_dangereux = (df_DRONE['DANGEREUX'].value_counts() / total2 * 100).tolist()
    pourc_dangereux = pour_dangereux[1]

    list_contrat = pd.unique(df_DRONE['CONTRAT']).tolist()
    total2 = df_DRONE['CONTRAT'].value_counts().sum()
    pour_contrat = (df_DRONE['CONTRAT'].value_counts() / total2 * 100).tolist()
    pourc_contrat = pour_contrat[2]
    leni = len(df_DRONE)

    prix_list = df_DRONE['PRIX'].tolist()

    df_DRONE1 = df1.loc[lambda x: x['DRONE/VEH'] == 'VÉHÉCULE ÉLÉCTRIQUE AUTONOME']
    df_per = df_DRONE1.loc[lambda x: x['ENT/PER'] == 'Personne']
    df_ent = df_DRONE1.loc[lambda x: x['ENT/PER'] == 'Entreprise']
    L = [(len(df_per.index) * 100) / len(df_DRONE)]
    L1 = [(len(df_ent.index) * 100) / len(df_DRONE)]

    leni = len(df_DRONE)
    # latitude = df1['depart_latitude'].to_list
    # longitude = df1['depart_longitude'].to_list

    context = {"mean_passagers": mean_passagers, "mean_poids": mean_poids, "mean_freqence": mean_freqence,
               "today": today, "mean_distance": mean_distance, "pour_fragile": pour_fragile,
               "pour_dangereux": pour_dangereux, "pour_contrat": pour_contrat,
               "list_fragile": list_fragile, "list_dangereux": list_dangereux, "list_contrat": list_contrat,
               "pourc_contrat": pourc_contrat, "pourc_fragile": pourc_fragile, "pourc_dangereux": pourc_dangereux,
               " leni": leni, "mean_distance_km": mean_distance_km, "prix_list": prix_list, "L": L, "L1": L1, }

    return render(request, 'intellapp/MAROC2.html', context)


def hi7(request):
    # Filter data to FRANCE

    today = datetime.now().ctime()
    context = {
        "today": today, }

    return render(request, 'intellapp/form_validation.html', context)


def hi8(request):
    # Filter data to FRANCE

    data = df.head(3)
    data = df.head(3)
    today = datetime.now().ctime()
    context = {"data": data,
               "today": today, }

    return render(request, 'intellapp/basic_table.html', context)


def hi10(request):
    # Filter data to FRANCE

    today = datetime.now().ctime()

    line_heuteur = df2['hauteur en ft'].to_list()
    temperature = df2['temperature en °C'][0:6].to_list()

    x = len(df2) - 1

    time = df2.Date_minute[x - 12:x].to_list
    temp = [df2['temperature en °C'][x], max(df2['temperature en °C'] - df2['temperature en °C'][x])]

    humidité = [df2['Humidité en  m/mer'][x], max(df2['Humidité en  m/mer'] - df2['Humidité en  m/mer'][x])]
    vent = [df2['Vitesse de vent en m/s'][x], max(df2['Vitesse de vent en m/s'] - df2['Vitesse de vent en m/s'][x])]
    vitesse = [df2['Vitesse en km/h'][x], max(df2['Vitesse en km/h'] - df2['Vitesse en km/h'][x])]
    internet = [df2['Vitesse internet en Mb/s'][x],
                max(df2['Vitesse internet en Mb/s'] - df2['Vitesse internet en Mb/s'][x])]

    temp_list = df2['date_time'].tolist()

    maxv = df2['Vitesse de vent en m/s'][x]
    print("maxv", maxv)
    maxvspeed = max(df2['Vitesse en km/h'])
    maxvspeed2 = max(df2['Vitesse en km/h']) * 3 / 4
    maxvspeed3 = max(df2['Vitesse en km/h']) / 2
    maxvt = df2['Vitesse en km/h'][x]

    maxvi = df2['Vitesse internet en Mb/s'][x - 1]
    L = []
    for i in range(0, x):
        L.append(i)

    line_temp = df2['temperature en °C'].to_list()
    line_humidité = df2['Humidité en  m/mer'].to_list()

    # map
    latitude = df2['latitude']
    longitude = df2['longitude']

    puissance = (df2['puissance en V'][x - 5:x]).to_list
    tension = (df2['tension électrique en m/s'][x - 5:x]).to_list
    intensité = ((df2['intensité du courant électrique en A'][x - 5:x]) / 100).to_list
    pression = (df2['pression en bar'][x - 5:x]).to_list

    context = {"today": today, "time": time, "temperature ": temperature, "temp": temp, "humidité": humidité,
               "vent ": vent, "vitesse": vitesse, "internet": internet, "temp_list": temp_list, "maxv": maxv,
               "maxvspeed": maxvspeed, "maxvspeed2": maxvspeed2, "maxvspeed3": maxvspeed3, "maxvt": maxvt,
               "maxvi": maxvi, "line_temp": line_temp, "line_humidité": line_humidité, "line_heuteur": line_heuteur,
               "L": L, "latitude": latitude,
               "longitude": longitude, "puissance": puissance, "tension": tension, "intensité": intensité,
               "pression": pression, }

    return render(request, 'intellapp/capteurs_drone.html', context)


def hi11(request):
    # Filter data to FRANCE

    today = datetime.now().ctime()

    time = df2.Date_minute[:12].to_list()
    line_heuteur = df2['hauteur en ft'].to_list()
    temperature = df2['temperature en °C'][0:6].to_list()

    x = len(df2) - 1
    temp = [df2['temperature en °C'][x], max(df2['temperature en °C'] - df2['temperature en °C'][x])]

    humidité = [df2['Humidité en  m/mer'][x], max(df2['Humidité en  m/mer'] - df2['Humidité en  m/mer'][x])]
    vent = [df2['Vitesse de vent en m/s'][x], max(df2['Vitesse de vent en m/s'] - df2['Vitesse de vent en m/s'][x])]
    vitesse = [df2['Vitesse en km/h'][x], max(df2['Vitesse en km/h'] - df2['Vitesse en km/h'][x])]
    internet = [df2['Vitesse internet en Mb/s'][x],
                max(df2['Vitesse internet en Mb/s'] - df2['Vitesse internet en Mb/s'][x])]

    temp_list = df2['date_time'].tolist()

    maxv = df2['Vitesse de vent en m/s'][x]
    print("maxv", maxv)
    maxvspeed = max(df2['Vitesse en km/h'])
    maxvspeed2 = max(df2['Vitesse en km/h']) * 3 / 4
    maxvspeed3 = max(df2['Vitesse en km/h']) / 2
    maxvt = df2['Vitesse en km/h'][x]

    maxvi = df2['Vitesse internet en Mb/s'][x - 1]
    L = []
    for i in range(0, x):
        L.append(i)

    line_temp = df2['temperature en °C'].to_list()
    line_humidité = df2['Humidité en  m/mer'].to_list()

    # map
    latitude = df2['latitude']
    longitude = df2['longitude']

    puissance = (df2['puissance en V'][x - 5:x]).to_list
    tension = (df2['tension électrique en m/s'][x - 5:x]).to_list
    intensité = ((df2['intensité du courant électrique en A'][x - 5:x]) / 100).to_list
    pression = (df2['pression en bar'][x - 5:x]).to_list

    context = {"today": today, "time": time, "temperature ": temperature, "temp": temp, "humidité": humidité,
               "vent ": vent, "vitesse": vitesse, "internet": internet, "temp_list": temp_list, "maxv": maxv,
               "maxvspeed": maxvspeed, "maxvspeed2": maxvspeed2, "maxvspeed3": maxvspeed3, "maxvt": maxvt,
               "maxvi": maxvi, "line_temp": line_temp, "line_humidité": line_humidité, "line_heuteur": line_heuteur,
               "L": L, "latitude": latitude,
               "longitude": longitude, "puissance": puissance, "tension": tension, "intensité": intensité,
               "pression": pression, }

    return render(request, 'intellapp/capteurs_vehicule.html', context)


''' def formulaire(request) :
    if request.method == "POST" :
        form = Forms(request.POST).save()
        return redirect('/formindex')
    else:
    form = Forms()

    context = {'form': form}
   return render(request, 'formindex.html')'''


def index(request):
    return render(request, 'intellapp/hi.html')
def index0(request):
    return render(request, 'intellapp/index0.html')

def green(request):
    today = datetime.now().ctime()
    c=df3.columns
    context = {"today": today,"c":c}


    return render(request, 'intellapp/capteurs_vehicule.html', context)



