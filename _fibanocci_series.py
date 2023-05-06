range_1 = 50
_first_number = 0
_second_number = 1
_third_number = 1

for i in range(0,range_1,1):

    if(_third_number < 50):
       print(_third_number,end=" ")
    _third_number = _first_number + _second_number
    _first_number = _second_number
    _second_number = _third_number
    