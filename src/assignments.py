from student.WordCounter import *
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
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},]
    def filter_males(people):
        return list(filter(lambda p: p['sex'] == "male", people_list))
    filtered_list = filter_males(people_list)
    print(filtered_list)

def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},]
    def calc_bmi(lst):
        list(map(lambda p: p.update({'bmi': (round(p['weight_kg'] / p['height_meters'] ** 2, 1))}), lst))
        return lst
    new_people_list = calc_bmi(people_list)
    print(new_people_list)
    
    return

def ex4():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},]
    def get_people(lst):
        return [i['name'] for i in lst if i['age'] >= 15]
    print(get_people(people_list))

def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.
    
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
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    return

if __name__ == "__main__":
    main()