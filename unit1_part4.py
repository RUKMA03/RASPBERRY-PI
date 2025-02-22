
>>> a


>>> impor t copy 


>>> a = ["it","was ","the ","best ","of", "ti mes"] 


>>> b = 
copy.copy
(a) 


>>> 
b.s or t
() 


>>> a


>>> b


>>>


>>> l = ["a","b", "c", "d"]


>>> l [
1:3
]


>>>


>>> l[
-
2
:] 


>>> l = ["
abc
","
def
","
ghi
","
ijk
"] 


>>> [
x.uppe r
()for x in l] 


for each elementof the l ist. 


>>> 
phone _nu mbe rs
= {'Simon':'
01234 567899
', 'Jane ':'
01234 666666
'} 


for all intents an d pur poses
v
ran dom. 


>>> phon e_numbers= {'Simon':'
01234 567899
', 'Jane':'
01234 
666666
'} 


>>> phon e_numbers['Simon']


>>> p hon e_numbers['Jane']


>>> 
phone_num bers
= {'Simon':'
01 23 4 56 78 99
','Jane':'
01 23 4 66 66 66
'} 


>>> 
phone_num bers
[' Phi l '] 


>>>


from the di ction ar y,where an unkn own key will cau sean  er ror.


>>> 
ph on e_n umbers
= {'Simo n':'
01234 567899
', 'Jan e':'
01234 
666666
'} 


>>> 
ph on e_n umbers .pop
('Jan e') 


>>> 
ph one _numbers


>>> phon e_numbers= {'Simon':'
01234 567899
', 'Jane':'
01234 
666666
'} 


>>> for namein phone_numbers: 


>>> 
ph one _numbers
= {'Simon':'
01234 567899
', 'Jane':'
01234 
666666
'} 


>>> for na me, 
num
in  
pho ne_nu mbers.items
():


>>> im p o r t 
RPi.GPIO
as GPIO 


>>> 
GPIO.setm o d e
(GPIO.B CM ) 


>>> 
GPIO.setu p
(
18
, GPIO.OUT) 


>>> 
GPIO.ou tp u t
(
18
, Tr u e ) 


>>> 
GPIO.ou tp u t
(
18
, False) 


GPIO. PWM to the actualfrequency on the pin measured wi than 
os cillo scope.


for the  LED modu le .


from the relayea ch time the contac ts are closed.


for example,whenyou
[
reswitchingAC (alternatingcurrent) or in 
situationswheretheexact wi ringof the device beingswi tched is 
unknow n.
