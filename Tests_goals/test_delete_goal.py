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


def test_delete_goal():

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

    print("STEP 2: Delete Goal")

    response = requests.delete(
        f"{BASE_URL}/goal/{goal_id}",headers=headers_variable
    )

    assert response.status_code == 200
    print("STEP 2 RESULT: Goal deleted")

    print("STEP 3: Get Goal (expect 404)")

    response = requests.get(
        f"{BASE_URL}/goal/{goal_id}",headers=headers_variable
    )

    assert response.status_code == 404
    print("STEP 3 RESULT: Goal not found")