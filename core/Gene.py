def make_list(list_model):
    serv_list=[]
    for i in range(len(list_model)):
    
        serv_list.insert(i,list_model[i][0])
        print("INDEX OF "+list_model[i][0]+" IS "+str(i))
    print("adjusted lists of nowww")
    print("->"*10)
    print(serv_list)
    print("->"*10)
    return serv_list