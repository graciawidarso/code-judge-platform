from api.config.logger import logger

data = {
    "id": "problem1_pdTuy",
    "title": "TwoSum",
    "description": "",
    "timeLimit": 3,
    "input": ["nums", "target"],
    "testCase": {
        "1": {"nums": [2, 7, 11, 15], "target": 9, "output": [0, 1]},
        "2": {"nums": [3, 2, 4], "target": 6, "output": [1, 2]},
        "3": {"nums": [3, 3], "target": 6, "output": [0, 1]},
        "4": {"nums": [-81, -10, -66, 11, 28, -37], "target": -91, "output": [0, 1]},
        "5": {"nums": [1, 2, 3], "target": 5, "output": [1, 2]},
        "6": {"nums": [9, 34, -54, 82, 22, -28], "target": 116, "output": [1, 3]},
        "7": {"nums": [17, 22, 61, -3, -31, 52, 89, -56], "target": 21, "output": [4, 5]},
        "8": {"nums": [-80, 67, -13, 22, -50, 53, -34, 39], "target": 40, "output": [2, 5]},
        "9": {"nums": [92, 1, 42, 95], "target": 187, "output": [0, 3]},
        "10": {"nums": [86, 41, -63, -26, -30, -42, -16, 53, -90], "target": 44, "output": [0, 5]},
        "11": {"nums": [12, 4, -11, 81, -13, 8, -38, -9, -78, -57, 32, -22, -80, 9], "target": 43, "output": [3, 6]},
        "12": {"nums": [-6, -18, 40, -48, 70, -16, -33, -45, -40, 64], "target": -93, "output": [3, 7]},
        "13": {"nums": [-23, 54, -39, -28, -36, 22, -7, 47, 1, -68, 16, 95, 17, -35, -64], "target": -51, "output": [0, 3]},
        "14": {"nums": [-61, -41, -23], "target": -84, "output": [0, 2]},
        "15": {"nums": [-51, -50, -27, -75, -64, -22, 91, -5, 67, 15, 13, -89, 42], "target": 106, "output": [6, 9]},
        "16": {"nums": [72, 21, 61, 44, 74, 60, 68, 79, 42], "target": 135, "output": [2, 4]},
        "17": {"nums": [128, 119, 11, 59, 144, 81, 107, 15, 127, -22, 97, 48, 18, 42], "target": 272, "output": [0, 4]},
        "18": {"nums": [43, 48, -12, 97, 111], "target": 145, "output": [1, 3]},
        "19": {"nums": [25, 59, 90, 63, 84, 85, 138, 112], "target": 148, "output": [3, 5]},
        "20": {"nums": [-2, 131, -12, 64, 61, 30, -11, -15, 74, 25, 99], "target": -14, "output": [0, 2]},
        "21": {"nums": [31, 130, 125, 16, 37, 146, -15, 137, 43], "target": 283, "output": [5, 7]},
        "22": {"nums": [-29, 76, 148, -13, 54], "target": 202, "output": [2, 4]},
        "23": {"nums": [107, 66, -29, 91, -14, -8, 0, 26, 95, 120, 132, 60, 52], "target": 112, "output": [5, 9]},
        "24": {"nums": [26, 93, 148, 54, 98, 95, 21, 114, 80, 10, 25, 22, 45, 140, 13], "target": 152, "output": [3, 4]},
        "25": {"nums": [96, -28, -15, -5, 142, -2, 133, 78, 121, -29, 127, -14, 36, 92, 27], "target": 64, "output": [1, 13]},
        "26": {"nums": [125, 23, 9, 61, 16], "target": 84, "output": [1, 3]},
        "27": {"nums": [98, 104, 64, 66, 131], "target": 130, "output": [2, 3]},
        "28": {"nums": [145, -3, 148, 6, 146, -20, 59], "target": 3, "output": [1, 3]},
        "29": {"nums": [57, 121, 145, 148, 15, -6, 81, 18], "target": 293, "output": [2, 3]},
        "30": {"nums": [145, 8, -18, 30, -1, 6, 77, 60, 12, 113, -30, 15, 142, -2, 149], "target": 59, "output": [2, 6]},
        "31": {"nums": [129, 7, 132, -25, 4, 116, 56, 101, 26, 107], "target": 236, "output": [0, 9]},
        "32": {"nums": [146, 140, 123, 116, 41, 64, 11, 75, 2, 118, 106, 71, 84], "target": 239, "output": [2, 3]},
        "33": {"nums": [71, 122, 24, 85, 3, 148, 86, 20, 14], "target": 95, "output": [0, 2]},
        "34": {"nums": [79, 38, 105, 37, -7, 120, 19, 102, 133, 44, 58, 41], "target": 199, "output": [0, 5]},
        "35": {"nums": [37, 111, 50, 146, 84, -22, 148, -20, 66], "target": 183, "output": [0, 3]},
        "36": {"nums": [127, -11, 52, 94, 149, 16, -6, -30, 85, 2, 4, -12, 146, 109, 89], "target": 153, "output": [4, 10]},
        "37": {"nums": [141, -1, -21, 5, 20, 73, -13, 93, 109, 71, 29, 83, -29, 97, 124], "target": 19, "output": [1, 4]},
        "38": {"nums": [12, 39, 28, 90], "target": 40, "output": [0, 2]},
        "39": {"nums": [85, 48, 5, 80, 37, 75], "target": 123, "output": [1, 5]},
        "40": {"nums": [7, 48, 144, 72, 68, 75], "target": 82, "output": [0, 5]},
        "41": {"nums": [93, 129, 132, 98, 13, 82, 48], "target": 222, "output": [0, 1]},
        "42": {"nums": [69, 67, -12, -28, 41, -13, 46, 103, 44], "target": 91, "output": [2, 7]},
        "43": {"nums": [32, 2, -28, -2, 19, 47], "target": -30, "output": [2, 3]},
        "44": {"nums": [-21, 107, 120, 148, 22, -19, 147, 128, -13, 131, -12, 45, 55], "target": 170, "output": [3, 4]},
        "45": {"nums": [-25, 65, -12, -24, 8, 131, 149], "target": 107, "output": [3, 5]},
        "46": {"nums": [40, 31, 47, -10, 65, 127, 19, 104, 0, 32, -6, 140, 125, 57, -23], "target": 161, "output": [7, 13]},
        "47": {"nums": [-25, 113, 143, 96, 12, 20, 99, 75, 64, 142], "target": 155, "output": [2, 4]},
        "48": {"nums": [103, 73, -10, 144, 128, 53, 65, 60, -15, 146, 74, -28], "target": 247, "output": [0, 3]},
        "49": {"nums": [80, 19, 37, 103, 40, 46, 61, -4, 66, 11, 90, 56, -2, 38], "target": 127, "output": [2, 10]},
        "50": {"nums": [116, -12, 149], "target": 104, "output": [0, 1]},
        "51": {"nums": [6, -9, 70, 72, 93], "target": 99, "output": [0, 4]},
        "52": {"nums": [1, 9, -8, 139, 29, -9, 131, 25, 97, -12], "target": 54, "output": [4, 7]},
        "53": {"nums": [-8, 1, 29, -15, 28, 31, -3, 128, 55, 149, 24, 121, 119], "target": -18, "output": [3, 6]},
        "54": {"nums": [15, 103, 31, 94, 18, -12, 70, 101, 108], "target": 49, "output": [2, 4]},
        "55": {"nums": [-6, -1, 87, 101, -7, 69, -22, 30, 49, 138, 85, 60], "target": 79, "output": [0, 10]},
        "56": {"nums": [-18, 111, 94, 147, 123, 81, 39], "target": 241, "output": [2, 3]},
        "57": {"nums": [67, 103, 18, -1, 147], "target": 170, "output": [0, 1]},
        "58": {"nums": [111, 15, 69, 8, 129, 101, 67, 17, 90, -17, 105], "target": 25, "output": [3, 7]},
        "59": {"nums": [-22, 23, -20, -27, 71, 51, -6, 112, 4, 125, 100, -14, 62], "target": 56, "output": [6, 12]},
        "60": {"nums": [27, 113, 65, 91, 48, 90, 123, -9, 62], "target": 81, "output": [5, 7]},
        "61": {"nums": [-30, 81, 148], "target": 51, "output": [0, 1]},
        "62": {"nums": [43, 64, 9, 52], "target": 116, "output": [1, 3]},
        "63": {"nums": [36, 119, 30, 122, 142, 66, -4, -29, 74, 93], "target": 89, "output": [6, 9]},
        "64": {"nums": [57, 0, 130, 149, -19, -7], "target": 111, "output": [2, 4]},
        "65": {"nums": [129, 1, 121, 20, 27, 86, 124, 38, 41, 33, 54, 84, 100, -6, 141], "target": 118, "output": [6, 13]},
        "66": {"nums": [105, 58, 55, 59, -16, -20, 69, 56, 121, 17, 39, 87], "target": 19, "output": [5, 10]},
        "67": {"nums": [49, 105, 32, 92, 36, 1], "target": 137, "output": [1, 2]},
        "68": {"nums": [104, 56, 143, 106, 5, 49, 25, 103, 122, 127], "target": 74, "output": [5, 6]},
        "69": {"nums": [7, 11, 107, 78, 80, 69, 108, 136, 68], "target": 215, "output": [2, 6]},
        "70": {"nums": [48, 34, 96, 128, 90, 80, 20, 47, 121, 51, 74, 140, 54, 2, 78, 31], "target": 249, "output": [3, 8]}, 
        "71": {"nums": [98, 16, 29, 144, 4, 62], "target": 78, "output": [1, 5]}, 
        "72": {"nums": [58, 67, 60, 119, 140], "target": 259, "output": [3, 4]}, 
        "73": {"nums": [133, 127, 86, 121, 89, 99, 6, 2, 109, 110], "target": 237, "output": [1, 9]}, 
        "74": {"nums": [69, 36, 14, 147, 116, 132, 6, 30], "target": 161, "output": [2, 3]}, 
        "75": {"nums": [142, 37, 133, 6, 104, 30, 83, 105], "target": 135, "output": [5, 7]}, 
        "76": {"nums": [11, 91, 128, 107, 114, 12, 55, 51, 138, 53, 38, 61, 27, 40, 16, 65], "target": 191, "output": [8, 9]}, 
        "77": {"nums": [142, 116, 1, 78, 27, 64, 77, 103, 56, 33, 35, 52, 20, 94, 118, 92, 69, 135, 16], "target": 68, "output": [9, 10]}, 
        "78": {"nums": [62, 100, 59, 125, 55, 39, 86, 40, 47, 104, 136, 126, 64, 33, 105, 21, 120, 35, 29], "target": 109, "output": [0, 8]}, 
        "79": {"nums": [29, 134, 47, 149, 126, 143, 137, 61, 79, 68, 8, 77], "target": 151, "output": [5, 10]}, 
        "80": {"nums": [109, 87, 69, 11, 126, 139, 41, 6, 44, 90, 4, 62, 45, 124, 98, 120, 27, 28], "target": 68, "output": [6, 16]},
        "81": {"nums": [18, 14, 123, 45, 56], "target": 32, "output": [0, 1]}, 
        "82": {"nums": [42, 92, 51, 11, 67, 100, 18, 60, 49, 149, 135, 68, 16, 34, 136, 130, 141, 55, 125], "target": 151, "output": [2, 5]}, 
        "83": {"nums": [85, 25, 118, 84, 104, 119, 12, 36, 3, 95, 122, 106, 67, 70, 27, 91], "target": 155, "output": [0, 13]}, 
        "84": {"nums": [63, 73, 145, 67, 71], "target": 208, "output": [0, 2]}, 
        "85": {"nums": [110, 74, 123, 94, 3], "target": 184, "output": [0, 1]}, 
        "86": {"nums": [114, 43, 56, 44, 149], "target": 158, "output": [0, 3]}, 
        "87": {"nums": [67, 55, 138, 53, 71, 142, 95, 109, 34, 50, 40, 97, 90, 129, 51, 28, 75, 65, 133], "target": 230, "output": [11, 18]}, 
        "88": {"nums": [123, 46, 29, 109, 90, 85, 113, 43], "target": 138, "output": [2, 3]}, 
        "89": {"nums": [117, 120, 125, 97, 95, 111, 47, 17, 115, 4, 100, 85, 57, 34, 40, 28, 7, 66, 87], "target": 64, "output": [6, 7]}, 
        "90": {"nums": [105, 66, 117, 81, 90, 109, 148, 132, 65, 92, 49, 116], "target": 238, "output": [4, 6]}, 
        "91": {"nums": [26, 148, 63, 106, 85, 127, 86, 114, 59, 3, 80, 98, 51, 67, 120, 55], "target": 130, "output": [2, 13]}, 
        "92": {"nums": [76, 78, 83, 143, 60, 14, 74, 111, 63, 10, 127, 90, 136, 7, 131, 141, 20, 128], "target": 174, "output": [7, 8]}, 
        "93": {"nums": [25, 10, 93, 94, 138, 108, 3, 126, 107, 101, 13, 32, 84, 106, 59, 83, 8, 30, 21, 120], "target": 167, "output": [5, 14]}, 
        "94": {"nums": [19, 71, 63, 134, 18, 60, 77, 64, 85, 65, 124, 40, 22, 119, 76, 139, 110, 26, 67, 20], "target": 184, "output": [5, 10]}, 
        "95": {"nums": [139, 93, 137, 101, 66, 74, 12], "target": 105, "output": [1, 6]}, 
        "96": {"nums": [20, 97, 96, 121, 57, 131, 51, 146, 109, 110, 77, 32, 149, 60, 38, 64, 81, 137], "target": 230, "output": [3, 8]}, 
        "97": {"nums": [134, 88, 109, 29, 53, 143, 13, 11, 68, 113, 135, 28, 124], "target": 57, "output": [3, 11]}, 
        "98": {"nums": [53, 6, 1, 34, 74, 119, 148, 82, 9, 131, 116, 97], "target": 153, "output": [3, 5]}, 
        "99": {"nums": [12, 125, 58, 101, 39, 10, 36, 142], "target": 135, "output": [1, 5]},
        "100": {"nums": [791, 606, 900, 248, 371, 332, 742, 740, 416, 552, 758, 983, 981, 829, 922, 682, 618], "target": 1812, "output": [11, 13]},
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
            logger.info(f"case id {id} start")
            nums = case.get("nums")
            target = case.get("target")
            expected_ouput = case.get("output")

            test_nums = nums.copy()
            test_target = target
            user_result = user_function(test_nums, test_target)

            try:
                # check if the user_result can be sorted
                sorted_user_result = sorted(user_result)

                # check if all of the user_result is all int
                is_all_int = all(isinstance(element, int)
                                for element in sorted_user_result)
                if is_all_int:
                    user_result = sorted_user_result
            except Exception:
                pass

            if expected_ouput == user_result:
                correct_case.append(id)
            else:
                false_case.append(id)
                if false_data is None:
                    false_data = f"<br>Given input:<br>&nbsp;&nbsp;&nbsp;&nbsp;nums: {nums}<br>&nbsp;&nbsp;&nbsp;&nbsp;target: {target}<br>Expected Output: {expected_ouput}<br>Your Result: {user_result}"
        result = {
            "caseCorrect": f"{len(correct_case)}/{total_case}",
            "feedback": false_data
        }
        return result, None
    except Exception as e:
        return None, f"test_problem failed: {e}"


