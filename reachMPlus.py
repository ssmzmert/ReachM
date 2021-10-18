# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:10:05 2021

Bu kod, Reach M+ tarafindan elde edilen konum bilgilerini (.csv dosyasini) 
okur ve kullanicinin secilen iki nokta arasindaki mesafeyi ogrenmesini saglar.

@author: Mert Sasmaz
"""

import pandas as pd
from math import cos, asin, sqrt, pi
#import mysql.connector

#Dosya acilir ve isim, enlem, boylam alinarak bir tablo olusturulur.
veriler = pd.read_csv('Deneme.csv')
print(veriler)
length = len(veriler)

data = pd.DataFrame(data=veriler, columns=['name', 'longitude', 'latitude'])
print(data)
print('#################################\n')

#Her bir nokta icin bir object yaratilir.
class Point:
  def __init__(self, name, longitude, latitude):
    self.name = name
    self.lon = longitude
    self.lat = latitude

#Verideki nokta kadar object ismi olusturulur. 
point = []
for i in range(length):
    point.append(i)

#Veriler objelere atanır.
for i in range(length):
    point[i] = Point(data.iloc[i, 0], data.iloc[i, 1], data.iloc[i, 2])

#iki nokta arasindaki uzakligi bulmak icin kullanilan fonksiyon(km).
#This script calculates great-circle distances between the two points
# – that is, the shortest distance over the earth’s surface – using the ‘Haversine’ formula.
def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a)) #2*R*asin...

print('Total', length, ' Nokta Bulunmaktadir')
for i in range(length):
    print(i, '-', point[i].name)
print('(Cikmak icin "exit" yaz)')
print('')
"""
#database ve table olusturduktan sonra konum 
#noktalarini isimleriyle birlikte veri tabanina isler.

def database(point):
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword"
    )

    print(mydb)

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")
    mycursor.execute("CREATE TABLE konumlar (name VARCHAR(255), longitude VARCHAR(255), latitude VARCHAR(255))")
    for i in range(length):
        sql = "INSERT INTO konumlar (name, longitude, latitude) VALUES (%s, %s, %s)"
        val = (point[i].name, point[i].longitude, point[i].latitude)
        mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
"""
count = 0

while(True):
  
    print('Mesafesini Bulmak Istediginiz Iki Noktanin Indexlerini Giriniz')

    no1 = input('Nokta 1: ')
    if no1 == 'exit':
        break
    else:
        no1 = int(no1)
        while(no1 not in range(0, length)):
            print('Gecersiz Index!')
            no1 = input('Nokta 1: ')
            if no1 == 'exit':
                count = 1
                break
            else:
                no1 = int(no1)
    if count == 1:
        break
    no2 = input('Nokta 2: ')
    if no2 == 'exit':
        break
    else:
        no2 = int(no2)
        while(no2 not in range(0, length)):
            print('Gecersiz Index!')
            no2 = input('Nokta 2: ')
            if no2 == 'exit':
                count = 1
                break
            else:
                no2 = int(no2)
        if count == 1:
            break
        res = distance(point[no1].lat, point[no1].lon, point[no2].lat, point[no2].lon)
        res = res * 100     #Kilometre'den Metre'ye cevirir.

        formatted_string = "{:.3f}".format(res) #Nokta sonrasi sadece 3 rakami saklar. Ex 4.6846541661 to 4.684
        res = float(formatted_string)
        print('\n',point[no1].name, ' ve ', point[no2].name, ' arasindaki mesafe, ', res, 'm dir.\n')