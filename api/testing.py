# import requests
# import json

# url = "http://127.0.0.1:5000/submit-answer"

# coding_text = """
# def ans(nums: list, target: int) -> list:
#     for index, num in enumerate(nums):
#         if ((target-num in nums) and (index != nums.index(target-num))):
#             return [index, nums.index(target-num)]
# """

# import multiprocessing
# import time

# def my_function(queue, arg1, arg2):
#     print(f"Function is starting with arguments: {arg1}, {arg2}")
#     time.sleep(2)  # Simulating a task
#     result = f"Result with {arg1}, {arg2}"
#     queue.put(result)
#     print("Function has finished")

# def run_with_timeout(func, timeout, *args):
#     queue = multiprocessing.Queue()
#     process = multiprocessing.Process(target=func, args=(queue,) + args)
#     process.start()
#     process.join(timeout)
#     if process.is_alive():
#         print("Function is taking too long, terminating it")
#         process.terminate()
#         process.join()
#         return None
#     else:
#         return queue.get()  # Get the result from the queue



# from api.utils import get_user_function, check_problem


# def ans(arr):
#     print(f"arr awal: {arr}")
#     carry=1
#     for i in range(len(arr)-1,-1,-1):
#         arr[i]+=carry
#         carry=arr[i]//10
#         arr[i]%=10
#     if carry:
#         arr.insert(0,carry)
#     print(f"arr akhir: {arr}")
#     return arr

def ans (arr):
    arr = [1,2,5]
    num = int (''.join(map(str,arr))) + 1
    result = [int(digit)for digit in str(num)]
    print(result)
    return (arr)

from api.resources.problems.problem_7 import data

if __name__ == '__main__':
    cases = data.get("testCase")

    for id, case in cases.items():
        arr = case.get("arr")
        exp_output = case.get("output")

        user_result = ans(arr)
        if user_result != exp_output:
            print(f"given input: {arr}, user result: {user_result}, exp output: {exp_output}")



    # filename = "k5mIz9NmCc-1702272753"
    # problem_id = "problem1_pdTuy"
    
    # user_function, error = get_user_function(filename)
    # result, error = check_problem(user_function, problem_id)
    # print(f"final result: {result}, error: {error}")

    # result = run_with_timeout(my_function, 5, "argument1", "argument2")
    # if result is not None:
    #     print(f"Function returned: {result}")
    # else:
    #     print("No result returned (function timeout or terminated)")