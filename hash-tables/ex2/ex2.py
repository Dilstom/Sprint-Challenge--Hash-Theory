def reconstruct_trip(tickets):
    dic={}
    route = ['']*(len(tickets)-1)

    for i in tickets:
        dic[i[0]] = i[1]  # dic{ start: destination,  }
        if(i[0] == None):
            route[0] = i[1]
    for i in range(1, len(route)):
        if(route[i-1]) in dic:
            route[i]=dic[route[i-1]]
        else:
            return[]
    return route
    

 

if __name__ == '__main__':
      # You can write code here to test your implementation using the Python repl
    short_set = [
      (None, 'PDX'),
      ('PDX', 'DCA'),
      ('DCA', None)
    ]
    print(reconstruct_trip(short_set), ['PDX', 'DCA'])
