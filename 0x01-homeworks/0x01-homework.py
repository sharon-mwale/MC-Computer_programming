if __name__ =="__main__":
  def main():
    fun_of_dict()
    fun_of_list()
    fun_of_tuple()

  def fun_of_list():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    print(len(my_list))
    print(my_list[3])
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Original list: ", my_list)
    x = my_list.pop()
    print(x)

  def fun_of_tuple():
      tuple = (10, 20, 30, 40, 50) 
      print(len(tuple)) 
      i = tuple[4]
      print("4th Elements From Tuple: ", i)

  def fun_of_dict():
    my_dict = {"name":"john","age": 25,"country": "USA"}
    print(my_dict.get['name'])
    my_dict.update({'age': 26})
    print(my_dict.get['name'])

  
