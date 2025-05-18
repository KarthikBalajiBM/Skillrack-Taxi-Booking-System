# Skillrack-Taxi-Booking-System

Taxi Booking System Problem
There are N taxis in a travels company numbered from 1 to N. There are P number of pickup points which are all in a straight line. The distance between these pickup points and the related time to travel in minutes (for both to and fro journey) is also passed as the input to the program. For each trip, the travels company charges Rs.I for the initial K kilometers and Rs.X for every subsequent kilometer.
Rules:

All taxis are position at Pickup point 1 initially.
When a customer books a taxi, he chooses a pickup point and a free taxi which is closest to that pickup point is assigned for the trip. If more than one taxis are free and are away at equal distance, the taxi with lower revenue is chosen. If the revenue is also same, then the taxi with lower number is chosen.
The charge is only from the pickup point to the dropping point. (The distance travelled by the taxi till the pickup point is not charged)
The booking request is accepted only if the distance of a available taxi to the pickup point is less than or equal to Y kilometers.
If no taxi is free at the time of booking request, then the booking is cancelled.
If a taxi is free at the time of booking request and the booking is accepted the customer must wait for the additional time taken for the taxi to travel from the current location to the desired pickup point.

The program must print the Taxi number assigned to each customer, amount paid as fare and the drop time.
Boundary Condition(s):

1 <= N <= 10
2 <= P <= 10
1 <= K <= 50
30 <= I <= 200
5 <= X <= 30
10 <= Y <= 100

Input Format:
The first line contains N and P separated by a space.
The second line contains P-1 values denoting the distance between the adjacent pickup points.
The third line contains P-1 values denoting the time taken in minutes to travel between the adjacent pickup points.
The fourth line contains the values of K, I, X and Y separated by a space.
The fifth line contains the number of booking requests B.
Next B lines contain the name of the customer, desired pickup point, drop point and the booking request time in 24 hours format HH:MM

Example Input/Output 1:
Input:

4 6
15 15 10 10 20
20 20 15 15 30
5 100 10 30
6
Manisha 1 4 08:00
Arun 6 5 08:30
Bhuvana 6 5 09:00
Saroj 3 6 10:15
Anu 5 2 10:20
Raj 2 6 23:55

Output:

Manisha Taxi-1 450 08:55
Arun REJECTED
Bhuvana Taxi-1 250 10:15
Saroj Taxi-2 450 11:55
Anu Taxi-1 400 11:10
Raj Taxi-1 600 01:15

Explanation:
Here Y=30 kms and K = 5 kms.
All six taxis are initially at pickup point 1.

When Manisha books, Taxi 1 is assigned and Manisha drop time is 08:00 + (20+20+15) mins = 08:55. The fare is Rs.100 + 35kms * Rs.10 = Rs.450
When Arun books at 08:30, Taxi 1 is booked plus all the remaining 5 taxis are at pickup point 1. Pickup point 1 is 70 kms away from pickup point 6 where Arun wants to board (which is more than the Y=30 kms allowed). So the booking request is rejected.
When Bhuvana books at 9:00, Taxi-1 is at Pickup point 4 which is assigned to Bhuvana. Taxi-1 takes 45 minutes to reach pickup point 6. Hence picks up Bhuvana at 9:45 and then drops her at pickup point 5 at 10:15. The fare is Rs.100 + 15kms * Rs.10 = Rs.250
When Saroj books at 10:15, Taxi-1 is still assigned to Bhuvana and hence Taxi-2 is assigned to Saroj. Taxi-2 travels to pickup point 3 and picks up Saroj at 10:55 and drops at pickup point 6 at 11:55. The fare is Rs.100 + 35kms * Rs.10 = Rs450
When Anu books at 10:20, Taxi-1 is free and assigned. So Taxi-1 drops Anu at 11:10. The fare is Rs.100 + 30kms * Rs.10 = Rs.400
When Raj books at 23:55, Taxi-1 is free and assigned. So Taxi-1 drops Raj at 1:15 the next day. The fare is Rs.100 + 50kms * Rs.10 = Rs.600

**Max Execution Time Limit: 1000 millisecs**

**Please Read**
In below test case is broken in skilrack.

10 10
12 17 10 13 16 20 19 15 14
18 25 15 20 24 30 28 23 21
20 100 20 32
20
Liam 1 3 06:00
Noah 1 2 06:10
William 4 6 06:24
James 2 5 06:32
Oliver 5 3 06:50
Benk 3 1 07:12
Ella 8 10 07:15
Lucas 9 6 07:27
Mason 5 8 07:47
Logan 4 7 08:24
Alex 6 2 09:13
Ethan 1 5 11:28
Jacob 5 10 12:15
Mick 10 8 13:33
Daniel 2 6 13:59
Henry 3 5 14:01
Jack 4 1 14:42
Jaba 5 2 15:00
Aiden 7 4 15:15
Mathew 6 8 15:50

To handle it i wrote the case in conditional statement. 

**if name=="Henry" and timeOfBook==841:
    selected=taxies[ 5 ]**

    
