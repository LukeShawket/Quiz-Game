import requests
import time


def get_question(difficulty):
    question_dict = {}
    url = f"https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"
    for i in range(5):
        response = requests.get(url=url)
        if response.status_code == 200:
            question_list = response.json()['results']
            question_dict = {key : {"question": question_list[key]['question'], "answer": question_list[key]['correct_answer']} for key in range(10)}
            return question_dict
        elif response.status_code == 429:
            print("Too many requests. Retrying in 2 seconds...")
            time.sleep(2) # Wait for 2 seconds before retrying
        else:
            response.raise_for_status()
    raise Exception("Failed to get questions after 5 retries")