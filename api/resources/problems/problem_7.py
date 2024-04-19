data = {
    "id": "ibo1",
    "title": "",
    "description": "",
    "timeLimit": 5,
    "input": ["arr"],
    "testCase": {
        "1": {"arr": [2,5], "output": [2,6]},
        "2": {"arr": [4,1], "output": [4,2]},
        "3": {"arr": [9,9], "output": [1,0,0]},
        "4": {"arr": [2], "output": [3]},
        "5": {"arr": [2,3,2,1,1,4], "output": [2,3,2,1,1,5]},
        "6": {"arr": [1], "output": [2]},
        "7": {"arr": [6,2], "output": [6,3]},
        "8": {"arr": [7,6,2,7,0,3], "output": [7,6,2,7,0,4]},
        "9": {"arr": [7,7,2,0,0], "output": [7,7,2,0,1]},
        "10": {"arr": [2,8,9,7,2], "output": [2,8,9,7,3]},
        "11": {"arr": [7,7,8,3], "output": [7,7,8,4]},
        "12": {"arr": [1,9], "output": [2,0]},
        "13": {"arr": [7,9], "output": [8,0]},
        "14": {"arr": [3,0,6,1,9], "output": [3,0,6,2,0]},
        "15": {"arr": [5,9,4], "output": [5,9,5]},
        "16": {"arr": [7,9,5], "output": [7,9,6]},
        "17": {"arr": [6,2,6,6], "output": [6,2,6,7]},
        "18": {"arr": [5,4,8,9,5], "output": [5,4,8,9,6]},
        "19": {"arr": [5,2,8], "output": [5,2,9]},
        "20": {"arr": [4,4,8], "output": [4,4,9]},
        "21": {"arr": [3,5,9,9], "output": [3,6,0,0]},
        "22": {"arr": [4], "output": [5]},
        "23": {"arr": [5,8,1,0,5], "output": [5,8,1,0,6]},
        "24": {"arr": [9,9,9], "output": [1,0,0,0]},
        "25": {"arr": [1,8,6], "output": [1,8,7]},
        "26": {"arr": [5,6,3,0], "output": [5,6,3,1]},
        "27": {"arr": [1,9,1,4,6,0], "output": [1,9,1,4,6,1]},
        "28": {"arr": [2,3,1,6], "output": [2,3,1,7]},
        "29": {"arr": [2,0,2,2], "output": [2,0,2,3]},
        "30": {"arr": [6,4], "output": [6,5]},
        "31": {"arr": [7,5,2], "output": [7,5,3]},
        "32": {"arr": [8,9,6,6,8], "output": [8,9,6,6,9]},
        "33": {"arr": [1,5,7], "output": [1,5,8]},
        "34": {"arr": [8,4,4,8], "output": [8,4,4,9]},
        "35": {"arr": [8,1,1,2,8,9], "output": [8,1,1,2,9,0]},
        "36": {"arr": [0], "output": [1]},
        "37": {"arr": [6,3,0,5,2], "output": [6,3,0,5,3]},
        "38": {"arr": [6,8,3,2,8,9], "output": [6,8,3,2,9,0]},
        "39": {"arr": [8], "output": [9]},
        "40": {"arr": [7,0,7], "output": [7,0,8]},
        "41": {"arr": [2,1,0,7], "output": [2,1,0,8]},
        "42": {"arr": [8,9], "output": [9,0]},
        "43": {"arr": [7,7,4,7,0], "output": [7,7,4,7,1]},
        "44": {"arr": [1,7,1,8,6], "output": [1,7,1,8,7]},
        "45": {"arr": [3], "output": [4]},
        "46": {"arr": [5], "output": [6]},
        "47": {"arr": [4,1,6,3,3], "output": [4,1,6,3,4]},
        "48": {"arr": [3,1,8,3,7,9], "output": [3,1,8,3,8,0]},
        "49": {"arr": [6,2,5], "output": [6,2,6]},
        "50": {"arr": [7], "output": [8]}
    }
}


def test_problem(user_function):
    try:
        test_case = data.get("testCase")
        total_case = len(test_case)
        correct_case = []
        false_case = []
        false_data = None

        for id, case in test_case.items():
            arr = case.get("arr")
            expected_ouput = case.get("output")

            test_arr = arr.copy()
            user_result = user_function(test_arr)

            if expected_ouput == user_result:
                correct_case.append(id)
            else:
                false_case.append(id)
                if false_data is None:
                    false_data = f"<br>Given input:<br>&nbsp;&nbsp;&nbsp;&nbsp;arr: {arr}<br>Expected Output: {expected_ouput}<br>Your Result: {user_result}"

        result = {
            "caseCorrect": f"{len(correct_case)}/{total_case}",
            "feedback": false_data
        }

        return result, None
    except Exception as e:
        return None, f"test_problem failed: {e}"
