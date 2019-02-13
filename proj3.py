
import sqlite3
"""
Name: Mohamed Imran Mohamed Siddique
Assignment: Project 3
MCS 275

"""
def create_db_and_table():
    conn = sqlite3.connect("mydatabases.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS public_passenger_vehicle_table (vtype text, status text, make text, model text, year int, color text, fuel text, access text, city text, state text, code int)"
    cursor.execute(sql)
    cursor.close()

def add_information():
   
    conn = sqlite3.connect("mydatabases.db")
    cursor = conn.cursor()

    with open("Public_Passenger_Vehicle_Licenses.csv", "r") as f:
         for line in f:
             if not line.startswith("Vehicle Type"):
                L = line.split(",")
                vtype = L[0]
                status = L[1]
                make = L[2]
                model = L[3]
                year = L[4]
                color = L[5]
                fuel = L[6]
                access = L[7]
                city = L[8]
                state = L[9]
                code = L[10]
                sql = "INSERT INTO public_passenger_vehicle_table (vtype, status, make, model, year, color, fuel, access, city, state, code) VALUES (:vtype, :status, :make, :model, :year, :color, :fuel, :access, :city, :state, :code)"
                cursor.execute(sql, {"vtype":vtype, "status":status, "make":make, "model":model, "year":year, "color":color, "fuel":fuel, "access":access, "city":city, "state":state, "code":code})     
                conn.commit()
    cursor.close()

def display_all_db_data():
    conn = sqlite3.connect('mydatabases.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM public_passenger_vehicle_table" 
    columns = cursor.execute(sql)
    all_entries = columns.fetchall()
    for entry in all_entries:
        print(entry)  

def Question_number_Two():
    conn = sqlite3.connect('mydatabases.db')
    cursor = conn.cursor()
    sql1 = "SELECT COUNT(fuel) FROM public_passenger_vehicle_table"
    sql2 = "SELECT COUNT(*) FROM public_passenger_vehicle_table WHERE fuel = 'Hybrid';"
    lowest_number = cursor.execute(sql1).fetchone()[0]
    sum_number = cursor.execute(sql2).fetchone()[0]
    print("The percentage of Hybrid cars are: ")
    avg_year = (float(sum_number)/float(lowest_number))
    print ("{:0}%".format(avg_year*100))
    #print("\n")

def Question_number_Three():
    conn = sqlite3.connect('mydatabases.db')
    cursor = conn.cursor()
    sql3 = "SELECT SUM(year) FROM public_passenger_vehicle_table"
    sql4 = "SELECT count(*) FROM public_passenger_vehicle_table"
    sum_year = cursor.execute(sql3).fetchone()[0]
    total_year = cursor.execute(sql4).fetchone()[0]
    print("The average car is: ")
    print(sum_year/total_year)
    #print("\n")

def Question_number_Four():
    conn = sqlite3.connect('mydatabases.db')
    cursor = conn.cursor()
    sql5 = "SELECT COUNT(DISTINCT model) FROM public_passenger_vehicle_table"
    types_year = cursor.execute(sql5).fetchone()[0]
    print("The amount of different car models are: ")
    print(types_year)
    #print("\n")

def Question_number_Five():
    conn = sqlite3.connect('mydatabases.db')
    cursor = conn.cursor()
    sql6 = "SELECT `model` FROM `public_passenger_vehicle_table` GROUP BY `model` ORDER BY COUNT(*) DESC LIMIT 1;"
    common_type = cursor.execute(sql6).fetchone()[0]
    print("The most common vehicle model is: ")
    print(common_type)
    #print("\n")

def Question_number_Six():
    conn = sqlite3.connect('mydatabases.db')
    cursor = conn.cursor()
    sql7 = "SELECT `city` FROM `public_passenger_vehicle_table` GROUP BY `city` ORDER BY COUNT(*) DESC LIMIT 2; "
    common_type = cursor.execute(sql7).fetchall()
    print("The second most common city is: ")
    print(common_type[1])

def Question_number_Seven():
    conn = sqlite3.connect('mydatabases.db')
    cursor = conn.cursor()
    sql8 = "SELECT `code` FROM `public_passenger_vehicle_table` GROUP BY `code` ORDER BY COUNT(*) DESC LIMIT 1;"
    common_code = cursor.execute(sql8).fetchone()[0]
    print("The zip code that contains the most registered public passenger vehicles is: ")
    print(common_code)
    

def main():
    
    create_db_and_table()
    #add_information() commented out so it doesn't add the same information over and over
    #display_all_db_data()
    print("---- Question 1 ----\n")
    print("This file is 926 Kilobytes")
    print("---- Question 2 ----\n")
    Question_number_Two()
    print("---- Question 3 ----\n")
    Question_number_Three()
    print("---- Question 4 ----\n")
    Question_number_Four()
    print("---- Question 5 ----\n")
    Question_number_Five()
    print("---- Question 6 ----\n")
    Question_number_Six()
    print("---- Question 7 ----\n")
    Question_number_Seven()
    print("---- End ----\n")
main() 