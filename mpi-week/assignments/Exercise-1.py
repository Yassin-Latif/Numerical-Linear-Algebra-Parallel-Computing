#Exercise 1 : Hello World

# Question 1 :
COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()

print('hello world',RANK,SIZE)

# Question 2 :

print('hello world from the processor {:d} out of {:d}'.format(RANK, SIZE))

# Question 3:

if RANK == 0:
    print('Hello world from processor {:d} out of {}'.format(RANK,SIZE))
