import copy
# copying immutable object
# assignmet immutable  what does it do ?
_listOneImmutable = [1, 2, 3, 4, 5]
_listOneImmutableAssignment = _listOneImmutable
'''
         _listOneImmutable            _listOneImmutableAssignment   
                       \               /    
                          [1,2,3,4,5]
                             ||
            _listOneImmutable[0] = 7; _listOneImmutableAssignment[1] = 10 
                              ||
                         [7,10,3,4,5]
    so this  is not equivalent to  #shallow copy copy.copy 
'''


# copy.copy immutable what does it do ?
_listOneImmutable = [1, 2, 3, 4, 5]
_listOneImmutableASHallowCopy = copy.copy(_listOneImmutable)
'''
    A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains. so here it will construct a new object ,it will copy the value 
      since we have a primitive object
 _listOneImmutable            _listOneImmutableASHallowCopy
        \                                  /
                                         copy value
         \                                /
     [1,2,3,4,5]                     N[1,2,3,4,5]
          |                               |
    _listOneImmutable[0] = 7         _listOneImmutableASHallowCopy[0] = 22  
    \[7,2,3,4,5]                     \[22,2,3,4,5] 
'''


# copying mutable object
# assignmet what does it do ?
_listOnemutable = [[0, 1], [2, 3]]
_listOnemutableAssignment = _listOnemutable
'''
         _listOnemutable            _listOnemutableAssignment   
                              @ : share address
                       \               /     
                          [[0,1] , [2,3]]
            _listOnemutable[0] = 7; _listOnemutableAssignment[1][1] = 10 
                              ||
                         [7 , [10,3]]
'''


# copying mutable object
# copy.copy mutable what does it do ?
# so this not as doing a deep copy
_listOnemutable = [[0, 1], [2, 3]]
_listOneSHallowCopy = copy.copy(_listOnemutable)
'''
     A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains. so here it will construc a new object ,it will copy the address since 
      we have a non primitive type 
 _listOnemutable              _listOneImmutableAssignmentSHallowCopy
        \                                  /
                                           New Object N : 
                                           @ copy address
         \                                /
      [[0,1] , [2,3]]                 N:[[0,1] , [2,3]]
          |                               |
 _listOnemutable[0] = 7;             _listOneImmutableAssignmentSHallowCopy[1][1] = 22  
    \[7, [2, 3]]                        \ [[0,1] , [2,22]]

'''

# copy.copy mutable && copy.deepcopy mutable
_listOnemutable = [[0, 1], [2, 3]]
_listOneSHallowCopy = copy.copy(_listOnemutable)
_listOneDeepCopy = copy.deepcopy(_listOnemutable)
'''
    - A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains
      
    - A deep copy constructs a new compound object and then, recursively,
      inserts *copies* into it of the objects found in the original.
    _listOnemutable                        _listOneSHallowCopy                              _listOneDeepCopy
            \                                     /                                                / 
                                            New  Object N  :                                        New Object N
                                                 @ copy address                                      @D Deep Copy values
            \                                    /                                                  /
    [[0, 1], [2, 3] ]                      N :[[0, 1], [2, 3] ]                                 N:[[0, 1], [2, 3] ]
            |                                     |
    _listOnemutable[0] = 7;               _listOneSHallowCopy[1][1] = 22                 _listOneDeepCopy[0][0] = 87 
    _listOnemutable[1][0] = 8;            
       \[7, [8, 22] ]                          [[0,1] , [8,22] ]                           [[87, 1], [2, 3]]

'''
