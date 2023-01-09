import dis 



def func():
    #calculation = 1
    loc = {}
    exec("calculation = 3", globals(), loc)
    calculation = loc['calculation']
    #calculation = 5
    #print('hello world')
    #print('type:',type(calculation))
    print('calculation:', calculation)
    #print(dir())
    #return calculation

func()
print(globals())

dis.dis(
    func
)
