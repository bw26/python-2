# define your methods here.
# ex1() - ex10()
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},]   
    def sort_people(people_lst, field, asc_or_dsc):
        people_lst.sort(key=lambda p: p[field], reverse=True if asc_or_dsc == "desc" else False)
    sort_people(people_list, "weight","desc")
    print(people_list)

def ex2():
    return

def ex3():
    
    return

def ex4():
    
    return

def ex5():
    
    return

def ex6():
    
    return

def ex7():
    
    return

def ex8():
    
    return

def ex9():
    
    return

def ex10():
    
    return

def main():
    ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    return

if __name__ == "__main__":
    main()