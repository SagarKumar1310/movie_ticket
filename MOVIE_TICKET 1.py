# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:04:26 2021

@author: sagar kumar
"""

x = 10
booked_seat = 0
price_of_ticket = 0
total_income = 0
row = int(input('Enter the numbers of rows:'))
column = int(input('Enter the number of columns:'))
total_seat = row*column
booked_ticket_person = [[None for j in range(column)]for i in range(column)]

class seats:
    
    @staticmethod
    def movie_seats():
        seats_1  = {}
        for i in range(row):
            seat_row = {}
            for j in range(column):
                seat_row[str(j+1)] = 'S'
            seats_1[str(i)] = seat_row
        return seats_1
    
    @staticmethod
    def seat_per():
         per = (booked_seat/total_seat)*100
         return per
class_call = seats()
movie_seats = class_call.movie_seats()

while x != 0:
     print('1 for show the seats \n2 for buy a ticket \n3 for statistics',
           '\n4 for show booked ticket user info \n0 for exit')
     x = int(input('select option - '))
     if x == 1:
         if column < 10:
             for i in range(column):
                 print(i,end=' ')
             print(column)
         else:
            for i in range(10):
                print(i,end=' ')
            for i in range(10,column):
                print(i,end=' ')
            print(column)
        
         if column<10:
            for j in movie_seats.keys():
                print(int(j)+1, end=' ')
                for k in movie_seats[j].values():
                    print(k, end=' ')
                print()
         else:
            seats_num = 0
            for i in movie_seats.keys():
                if int(list(movie_seats.keys())[seats_num]):
                    print(int(i)+1, end=' ')
                else:
                    print(int(i)+1, end=' ')
                seats_keys = 0
                for j in movie_seats.values():
                    if int(list(movie_seats[i].keys())[seats_keys]):
                       print(int(j)+1, end=' ')
                else:
                     print(int(j)+1, end=' ')
                     seats_keys +=1
                seats_num +=1
                print()
         print('available seats= ',total_seat-booked_seat)
         print()
         
            
     elif x == 2:
        row_number = int(input('enter row number'))
        column_number = int(input('enter column number'))
        if row_number in range(1,row+1)and column_number in range(1,column+1):
            if movie_seats[str(row_number-1)][str(column_number)] == 'S':
                if row*column <=60:
                 price_of_ticket = 10
                elif row_number <= int(row/2):
                     price_of_ticket = 10
                else:
                     price_of_ticket = 8
                print('price_of_ticket - ','rs',price_of_ticket)
                confirm = input('yes for booking and no for stop booking - ')
                person_detail = {}
                if confirm == 'yes':
                  person_detail['name']=input('enter name - ')
                  person_detail['gender']=input('enter gender - ')
                  person_detail['age']=input('enter age - ')
                  person_detail['phone-no']=input('enter phone-no - ')
                  person_detail['ticket_price']=price_of_ticket
                  movie_seats[str(row_number-1)][str(column_number)] = 'B'
                  booked_seat +=1
                  total_income+=price_of_ticket
                else:
                   continue
                booked_ticket_person[row_number-1][column_number-1] = person_detail
                print('Booked Succesfully')
            else:
              print('This seat is already Booked')
        else:
          print()
          print('Invalid Input')
        print()
     
     
     elif x == 3:
         print('Number of purchased ticket - ',booked_seat)
         print('Per - ',class_call.seat_per())
         print('current income - ','rs',price_of_ticket)
         print('total_income - ',total_income)
         print()
         
     elif x == 4:
         enter_row = int(input('enter row number - \n'))
         enter_column = int(input('enter column number - \n'))
         if enter_row in range(1,row+1) and enter_column in range(1,column+1):
             if movie_seats[str(enter_row-1)][str(enter_column-1)] =='B':
                 person = booked_ticket_person[enter_row-1][enter_column-1]
                 print('Name - ',person['Name'])
                 print('Gender - ',person['Gender'])
                 print('age - ',person['Age'])
                 print('phone_no - ',person['Phone_no'])
                 print('total price - ','rs',person['ticket_price'])
             else:
                print()
                print('available seat')
                
         else:
            print()
            print('Invalid Input')
         print()
        
     else:
        print()
        print('Invalid Input')
        print()                                        
         
         
                    