import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")
TEAM_ID = os.getenv("TEAM_ID")
GOAL_NAME = os.getenv("GOAL_NAME")

headers_variable = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}


def test_post_goal_request():

    print("STEP 1: Create Goal")

    response = requests.post(
        f"{BASE_URL}/team/{TEAM_ID}/goal",headers=headers_variable,json={
            "name": GOAL_NAME,
            "team_id": TEAM_ID
        }
    )

    assert response.status_code == 200
    assert response.json()["goal"]["name"] == GOAL_NAME

    goal_id = response.json()["goal"]["id"]
    print(f"STEP 1 RESULT: Goal created ID = {goal_id}")

    print("STEP 2: DELETE Goal")

    response = requests.delete(
        f"{BASE_URL}/goal/{goal_id}",headers=headers_variable
    )

    assert response.status_code == 200

    print("STEP 2 RESULT: Goal deleted")