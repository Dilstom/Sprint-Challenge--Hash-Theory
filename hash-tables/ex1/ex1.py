def get_indices_of_item_weights(weights, limit):
    dic={}
    for i in range(len(weights)):
        if(limit-weights[i]) in dic:
            return(i, dic[limit-weights[i]])
        else:
            dic[weights[i]]=i;
    

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(get_indices_of_item_weights([4,6,10,15,6], 21))