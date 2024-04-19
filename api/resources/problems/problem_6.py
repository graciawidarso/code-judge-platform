data = {
    "id": "bs1",
    "title": "",
    "description": "",
    "timeLimit": 5,
    "input": ["a", "b"],
    "testCase": {
        "1": {"a": "001", "b": "01", "output": "010"},
        "2": {"a": "01011", "b": "0", "output": "01011"},
        "3": {"a": "10", "b": "01", "output": "11"},
        "4": {"a": "11001010", "b": "001010", "output": "11010100"},
        "5": {"a": "1101111", "b": "1010", "output": "1111001"},
        "6": {"a": "0111101", "b": "001", "output": "0111110"},
        "7": {"a": "10", "b": "01110", "output": "10000"},
        "8": {"a": "11", "b": "001", "output": "100"},
        "9": {"a": "010111", "b": "011101", "output": "110100"},
        "10": {"a": "110100", "b": "111", "output": "111011"},
        "11": {"a": "011000", "b": "01", "output": "011001"},
        "12": {"a": "10100011", "b": "01001", "output": "10101100"},
        "13": {"a": "111", "b": "1011", "output": "10010"},
        "14": {"a": "01010000", "b": "111", "output": "01010111"},
        "15": {"a": "01", "b": "100", "output": "101"},
        "16": {"a": "0111001", "b": "01011010", "output": "10010011"},
        "17": {"a": "0110", "b": "1", "output": "0111"},
        "18": {"a": "101", "b": "10010011", "output": "10011000"},
        "19": {"a": "101", "b": "001", "output": "110"},
        "20": {"a": "11", "b": "011100", "output": "011111"},
        "21": {"a": "11011001", "b": "1", "output": "11011010"},
        "22": {"a": "11110101", "b": "11", "output": "11111000"},
        "23": {"a": "01110", "b": "01110011", "output": "10000001"},
        "24": {"a": "11001010", "b": "001110", "output": "11011000"},
        "25": {"a": "001", "b": "1100", "output": "1101"},
        "26": {"a": "1", "b": "01000", "output": "01001"},
        "27": {"a": "101010", "b": "010011", "output": "111101"},
        "28": {"a": "011", "b": "1", "output": "100"},
        "29": {"a": "10011", "b": "11", "output": "10110"},
        "30": {"a": "0001", "b": "001", "output": "0010"},
        "31": {"a": "110111", "b": "11", "output": "111010"},
        "32": {"a": "0101110", "b": "0", "output": "0101110"},
        "33": {"a": "0001110", "b": "01101100", "output": "01111010"},
        "34": {"a": "10010011", "b": "101", "output": "10011000"},
        "35": {"a": "01", "b": "01111", "output": "10000"},
        "36": {"a": "0100", "b": "1110110", "output": "1111010"},
        "37": {"a": "101011", "b": "010100", "output": "111111"},
        "38": {"a": "011", "b": "100011", "output": "100110"},
        "39": {"a": "10", "b": "1011101", "output": "1011111"},
        "40": {"a": "1011", "b": "1010100", "output": "1011111"},
        "41": {"a": "00100", "b": "1011", "output": "01111"},
        "42": {"a": "10", "b": "111100", "output": "111110"},
        "43": {"a": "1010011", "b": "11101100", "output": "100111111"},
        "44": {"a": "101", "b": "111110", "output": "1000011"},
        "45": {"a": "11101", "b": "00100000", "output": "00111101"},
        "46": {"a": "1010111", "b": "1", "output": "1011000"},
        "47": {"a": "011", "b": "00110101", "output": "00111000"},
        "48": {"a": "00000001", "b": "101001", "output": "00101010"},
        "49": {"a": "01111101", "b": "001110", "output": "10001011"},
        "50": {"a": "1010100", "b": "1", "output": "1010101"}
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
            a = case.get("a")
            b = case.get("b")
            expected_ouput = case.get("output")

            test_a = a
            test_b = b
            user_result = user_function(test_a, test_b)

            if expected_ouput == user_result:
                correct_case.append(id)
            else:
                false_case.append(id)
                if false_data is None:
                    false_data = f"<br>Given input:<br>&nbsp;&nbsp;&nbsp;&nbsp;a: {a}<br>&nbsp;&nbsp;&nbsp;&nbsp;b: {b}<br>Expected Output: {expected_ouput}<br>Your Result: {user_result}"

        result = {
            "caseCorrect": f"{len(correct_case)}/{total_case}",
            "feedback": false_data
        }

        return result, None
    except Exception as e:
        return None, f"test_problem failed: {e}"
