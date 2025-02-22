>>> 
s.fi n d
("
def
") 


>>> 
122 


>>> s = "
abcdefghi
^


>>> s [
1:5
] 


>>> N otethat thecharacterpos itions startat 
0
, s o  apos itio no f  
1 
means the s econd characterinthe stringand 
5 
means the s ix th, but 
the characterrangeis exclusiveatthe high end, s o letterf not 
included


>>> 


>>> " my fi le.txt"[
-
3
:] 
'txt' 
describes joiningstringstogether 


>>> s = "It wasthe bestof X. It wasthe worstof X" 


>>> 
s. replace
("X","times")


>>> 


>>> "
aBcDe
". upper() 


>>> 


>>> "
aBcDe
". lo wer() 


>>>


>>> 
s.upper
() 
'ABCD E' 
>>> s
'
aBcD e
'       / / o riginalst ring unchange d/ /
>>> 


>>> s =  
s.upper
() 
>> >s 'ABCD E' 
>>> 


>>> x = 
101 
>>> if x > 
100
: 
. . . print("x is big") 
...
x is big


if x > 
100
: 
print("x is big") 
elif
x < 
10
: 
print("x is small") 
else: 
print("x is medium") 
This examplewil lprintx ismedium.


>>> 
1 
!= 
2 
Tru e
>>> 
1 
!= 
1 
Fal se 
>>> 
10 
>= 
10 
Tru e
>>> 
10 
>= 
11 
Fal se 
>>> 
10 
== 
10 
Tru e 


>>> 'aa'< ' ab' 
True 
>>> '
aaa
'< 'aa' 
False 


>>> x = 
17 
>>> if x >= 
10 
and x <= 
20
: . . .
print('x is inthe middle') . . .  


>>> for  
i
in range(
1
, 
11
):


>>> answer= ' ' 
>>> whileanswer!= 'X ':
. . . answer= input('Enter command:') 
. . . Enter 
command:A
Enter 
co mmand:B
Enter 
command:X
>>>


>>> whileTrue: 
. . . answer= i nput('Enter command:') 
. . . if answer== 'X' :
. . . break 
. . . Enter 
command:A
Enter 
co mmand:B
Enter 
co mmand:X
>>> 


print(
i
) 


>>> a = [
34
, 'Fred', 
12
, Fal se , 
72.3
] 


>>> 