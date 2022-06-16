import math
def calc(x0,A, H, X, e, alpha,A_const_eq,B_const_eq,C_const_eq,d,w,n):
  # inital check for x0
  if type(x0) != list:
    return "inproper type for x0"
  # inital check for C
  #if not C:
  #  return "define C"
  # inital check for H
    for i in H:
      if type(H) != list:
        return "inproper type for H"
      if type(i) != int:
        return "inproper type for H"
  # inital check for A
    for i in A:
      if type(A) != list:
        return "inproper type for A"
      if type(i) != list:
        return "inproper type for A"
  # inital check for X
      for i in X:
        if type(X) != list:
          return "inproper type for X"
      if type(i) != list:
        return "inproper type for Xn"
        for j in i:
          if type(j) != list:
            return "inproper type for Xn cords"
  # inital check for e
    if not e:
      return "define e"
    if not alpha:
      return "define alpha"
    if (e + alpha) == 0 or (e + alpha) > math.pi/2:
      return f"out of range e {e} and/or alpha {alpha}"
  
  # draw boards
  # A_const_equ,B_const_equ,C_const_equ = 0,0,0

  # G board equaiton
    #(A_const_equ * x) + (B_const_equ * y)  + (C_const_equ * z) = d
#def G_board(A_const_eq,B_const_eq,C_const_eq,d):
#  (A_const_equ * x) + (B_const_equ * y)  + (C_const_equ * z) = d

# H board equaiton
#(A_const_equ * x) + (B_const_equ * y)  + (C_const_equ * z) = d
#def H_board(A_const_eq,B_const_eq,C_const_eq,d,w):
  # return (A_const_equ * xline) + (B_const_equ * yline)  + (C_const_equ * zline) = d + w
#  (A_const_equ * x) + (B_const_equ * y)  + (C_const_equ * z) = d + w

# calc t
#G_board(xline,yline,zline)

  list_taghato=[]
  for i in range (0,n):
    t = ((d + w) - ((A_const_eq * X[i][0]) + (B_const_eq * X[i][1]) + (C_const_eq * X[i][2]))) / ((A_const_eq * A[i][0]) + (B_const_eq * A[i][1]) + (C_const_eq * A[i][2]) )
  
  # line equaiton intersection with vector
    xline = X[i][0] + (A[i][0] * t)
    yline = X[i][1] + (A[i][1] * t)
    zline = X[i][2] + (A[i][2] * t)
    list_taghato+=[[xline,yline,zline]]
  matris_mojaverat=[]
  for i in range(0,n-1):
    listA=[]
    for j in range(0,n-1):
      listA+=[dist(list_taghato[i],list_taghato[j])]
    matris_mojaverat+=[listA]
    listA=[]
  return (list_taghato)

def dist(A,B):
  dist=math.sqrt(math.pow(A[0]-B[0],2)+math.pow(A[1]-B[1],2)+math.pow(A[2]-B[2],2))
  return dist
  
################################################################ data vorodi #############
from random import seed
from random import randint
def vrodi():
    x0=[0,0,0]
    e=math.pi/4
    a1=math.pi/4
    alpha=math.pi /6
    A_const_eq=0
    B_const_eq=0
    C_const_eq=1
    d=0
    n=50
    #w=min(H)
    # generate random integer values
    # seed random number generator
    seed(1)
    # generate some integers

    Xf=[]
    for _ in range(n):
        li=[]
        for i in range(3):
            li+=[randint(0, 100)]
        Xf+=[li]
        li=[]

    A_size=[]
    for _ in range(n):
        val=randint(2, 100)
        A_size+=[val]
    H=[]
    for i in range(n):
        value = A_size[i] * math.sin((math.pi /2)-e)
        H+=[value]
    Xl=[]
    for i in range(n):
        value = [(A_size[i]*(math.sin(e))*(math.cos(a1)))+Xf[i][0],(A_size[i]*(math.sin(e))*(math.sin(a1)))+Xf[i][1],
        (A_size[i]*(math.cos(e)))+Xf[i][2]]
        Xl+=[value]
        value =[]

    A=[]
    for i in range(n):
        value = [Xl[i][0]-Xf[i][0] , Xl[i][1]-Xf[i][1] , Xl[i][2]-Xf[i][2] ]
        A+=[value]
        value =[]

    w=min(H)

    taghato =calc(x0,A, H, Xf, e, alpha,A_const_eq,B_const_eq,C_const_eq,d,w,n)
    taghato_on_h=[]
    for i in range (n):
        value=[]
        value+=[(taghato[i][0],taghato[i][1])]
        taghato_on_h+=[value[0]]
        value=[]
    print(taghato_on_h)
    return(taghato_on_h)

################################################################ tsp #####################
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model(list1):
    """Stores the data for the problem."""
    data = {}
    # Locations in block units
    #data['locations'] = [
    #    (5,5),(3,3),(9,9),(10,10),(2,3)
    #]  # yapf: disable
    data['locations'] =list1
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Euclidean distance
                distances[from_counter][to_counter] = (int(
                    math.hypot((from_node[0] - to_node[0]),
                               (from_node[1] - to_node[1]))))
    return distances


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Objective: {}m\n'.format(route_distance)


def main():


    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(vrodi())

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = compute_euclidean_distance_matrix(data['locations'])

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)


if __name__ == '__main__':
    main()
