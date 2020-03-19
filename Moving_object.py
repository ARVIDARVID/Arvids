import numpy as np
import math

def quit_sim(x,y):
##    print('The simulation succeeded:')
##    print('Input=0. Quit simulation. Result: x=',x,', y=',y)
    print(x,y)

    return

def forward(x,y,direction):
 #   print('direction[0]=',direction[0],'direction[1]=',direction[1])
    if direction[0]==0 and direction[1]==1:
        #Pointing to north
        x_new=x
        y_new=y-1
        
    elif direction[0]==1 and direction[1]==0:
        #Pointing to east
        x_new=x+1
        y_new=y
    elif direction[0]==0 and direction[1]==-1:
        #Pointing to south
        x_new=x
        y_new=y+1
    elif direction[0]==-1 and direction[1]==0:
        #Pointing to west
        x_new=x-1
        y_new=y

    return x_new,y_new

def backward(x,y,direction):
    if direction[0]==0 and direction[1]==1:
        #Pointing to north
        x_new=x
        y_new=y+1
        
    elif direction[0]==1 and direction[1]==0:
        #Pointing to east
        x_new=x-1
        y_new=y
    elif direction[0]==0 and direction[1]==-1:
        #Pointing to south
        x_new=x
        y_new=y-1
    elif direction[0]==-1 and direction[1]==0:
        #Pointing to west
        x_new=x+1
        y_new=y

    return x_new,y_new


def rot_clock(direction):
    n_dim=2
    new_direction=np.zeros(n_dim)
    rot_mat=np.zeros((2,2))
    rot_mat[0][0]=0
    rot_mat[0][1]=1
    rot_mat[1][0]=-1
    rot_mat[1][1]=0
    for i in range(n_dim):
        summa=0
        for j in range(n_dim):
            
            summa=summa+rot_mat[i][j]*direction[j]
            
        new_direction[i]=summa

    return new_direction

def rot_counterclock(direction):
    n_dim=2
    new_direction=np.zeros(n_dim)
    rot_mat=np.zeros((2,2))
    rot_mat[0][0]=0
    rot_mat[0][1]=-1
    rot_mat[1][0]=1
    rot_mat[1][1]=0
    for i in range(n_dim):
        summa=0
        for j in range(n_dim):
            
            summa=summa+rot_mat[i][j]*direction[j]
            
        new_direction[i]=int(summa)
      #  print('summa=',summa,'int(summa)=',int(summa),'new_direction[i]=',new_direction[i])

  #  print('new_direction[0]=',new_direction[0],'new_direction[1]=',new_direction[1])
    return new_direction

#EXTRA....
def rot_THETA(direction,THETA):
    import math
    n_dim=2
    new_direction=np.zeros(n_dim)
    rot_mat=np.zeros((2,2))
    rot_mat[0][0]=math.cos(THETA)
    rot_mat[0][1]=-math.sin(THETA)
    rot_mat[1][0]=math.sin(THETA)
    rot_mat[1][1]=math.cos(THETA)
    for i in range(n_dim):
        summa=0
        for j in range(n_dim):
            
            summa=summa+rot_mat[i][j]*direction[j]
            
        new_direction[i]=summa
      #  print('summa=',summa,'int(summa)=',int(summa),'new_direction[i]=',new_direction[i])

  #  print('new_direction[0]=',new_direction[0],'new_direction[1]=',new_direction[1])
    return new_direction


def moving_object(n,m,x0,y0):
    mat=np.zeros((n,m))
    x_max=n-1
    x_min=0
    y_max=m-1
    y_min=0

    A=[1,4,1,3,2,3,2,4,1,0]
##    A=[1,1,1,1,1,1,1,1,1,1]
##    A=[4,4,4,4]
##    A=[3,3,3,3]
    # [0,1] means north
    # [1,0] means east
    # [0,-1] means south
    # [-1,0] means west
    # Always start in north direction
    direction=[0,1]
    x=x0
    y=y0
    x_new=x
    y_new=y
    new_direction=direction

  #  print('n=',n,'m=',m,'x0=',x0,'y0=',y0,'direction=',direction)
    ctr=0
    num_in=1
    while num_in!=0:
##        print('ctr=',ctr) #,'A[ctr]=',A[ctr])
##        num_in=A[ctr]
        nb = input('Choose a number: ')
##        print('you entered:' + nb)
        
        num_in=float(nb) #A[ctr]
##        print('num_in=',num_in)
        
        if num_in==0:
            quit_sim(x,y)
            exit()
        elif num_in==1:
            x_new,y_new=forward(x,y,direction)
        elif num_in==2:
            x_new,y_new=backward(x,y,direction)
        elif num_in==3:
            new_direction=rot_clock(direction)
        elif num_in==4:
            new_direction=rot_counterclock(direction)
##        elif num_in==9:
##            THETA=math.pi/4
##            new_direction=rot_THETA(direction,THETA)

        if x_new>x_max or x_new<x_min or y_new>y_max or y_new<y_min:
            x=-1
            y=-1
##            print('The simulation failed')
##            print('Outside the matrix: x=',x,'y=',y)
            print(x,y)
            return x,y
        else:
            direction=new_direction
            x=x_new
            y=y_new
            
        ctr=ctr+1
##        print('x=',x,'y=',y,'direction=',direction)
    return x,y



#MAIN********************************************
nb = input('Enter size of x-dimension: ')
n=int(nb)
nb = input('Enter size of y-dimension: ')
m=int(nb)
nb = input('Enter starting position for x: ')
x0=int(nb)
nb = input('Enter starting position for y: ')
y0=int(nb)
moving_object(n,m,x0,y0)

