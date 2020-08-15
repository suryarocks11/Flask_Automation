def function1(Function):
    def exe ():
        print("Hellow program Starts")
        Function()
        print('Function Ends')
    return (exe)
@function1
def start_program():
    print('Surya is runnnig')

start_program()