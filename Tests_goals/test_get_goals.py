import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")
TEAM_ID = os.getenv("TEAM_ID")

headers_variable = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}


def test_get_goals():

    print("STEP 1: Get all Goals")
    response = requests.get(
        f"{BASE_URL}/team/{TEAM_ID}/goal",headers=headers_variable
    )

    assert response.status_code == 200
    goals = response.json()

    print(f"STEP 1 RESULT: Goals received. Count = {len(goals.get('goals', []))}")
    assert "goals" in response.json()
    print("STEP 2 RESULT: Response contains 'goals' key")