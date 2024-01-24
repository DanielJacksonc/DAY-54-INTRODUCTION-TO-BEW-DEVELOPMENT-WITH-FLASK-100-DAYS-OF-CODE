"""challenge: Create your own decorator function that measures the amount of seconds that a function takes to execute"""
import time
from flask import Flask
app = Flask(__name__)


current_time = time.time()
print(current_time) #seconds since jan 1st,1970

#write your code here
def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {start_time - end_time}")
    return wrapper_function




@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i + 1
@speed_calc_decorator
def slow_function():
    for i in range(100567):
        i + 1

fast_function()
slow_function()


# if __name__ == "__main__":
#     # app.run()
