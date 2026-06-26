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


def test_update_goal():

    print("STEP 1: Create Goal")

    response = requests.post(
        f"{BASE_URL}/team/{TEAM_ID}/goal",headers=headers_variable,json={
            "name": GOAL_NAME,
            "team_id": TEAM_ID
        }
    )
    assert response.status_code == 200

    goal_id = response.json()["goal"]["id"]
    print(f"STEP 1 RESULT: Goal created ID = {goal_id}")

    print("STEP 2: Update Goal")

    response = requests.put(
        f"{BASE_URL}/goal/{goal_id}",headers=headers_variable,json={
            "name": "Updated Goal Name"
        }
    )
    assert response.status_code == 200

    print("STEP 2 RESULT: Goal updated")

    print("STEP 3: Get Goal")

    response = requests.get(
        f"{BASE_URL}/goal/{goal_id}",headers=headers_variable
    )

    assert response.status_code == 200
    assert response.json()["goal"]["name"] == "Updated Goal Name"

    print("STEP 3 RESULT: Goal verified after update")

    print("STEP 4: Delete Goal")

    response = requests.delete(
        f"{BASE_URL}/goal/{goal_id}",headers=headers_variable
    )

    assert response.status_code == 200

    print("STEP 4 RESULT: Goal deleted")