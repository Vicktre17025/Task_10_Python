import json

import pytest
import requests
from pytest_steps import steps, test_steps

headers_variable = {
    'Authorization': 'pk_210233017_YNJBMSJ3HQNR4W3DGFT0ARZIIF6RUFXB',
    'Content-Type': 'application/json',
}


@pytest.fixture
def get_goal_id():
    with open ('./test_goal.json', 'r') as jsonFile:
        json_data = json.load(jsonFile)
        goal_id=json_data['id']
        return goal_id

def test_get_goal_request(get_goal_id):
    print(get_goal_id)
    #response = requests.get('https://api.clickup.com/api/v2/goal/c73746c8-84cf-44ee-bd6d-4c3d613ceaf6', headers=headers_variable)
    #assert response.status_code == 200
    #assert response.json()['goal']['id'] == 'c73746c8-84cf-44ee-bd6d-4c3d613ceaf6'





#задання параметрів для тесту
#@pytest.mark.parametrize('goal_id, response_status',[
    ##('c73746c8-84cf-44ee-bd6d-4c3d613ceaf6' ,200),
    #('2323232' ,404)
#])

#def test_get_goals_request():
    #response = requests.get('https://api.clickup.com/api/v2/team/90121772320/goal', headers=headers_variable)
    #assert response.status_code == 200
    #assert response.json()['goals'][0]['id'] == '0965b368-42d8-41f1-978b-c1e641d64eaa'
    #print(response.json())

#def test_post_goal_request():
    #response = requests.post('https://api.clickup.com/api/v2/team/90121772320/goal', headers=headers_variable, json={"name": "Goal Name11"})
    #assert response.status_code == 200

# тест з кроками та з використанням змін
#@test_steps ('Update Goal', 'Get Goal request')
#def test_put_goal_request(goal_id, response_status):
    #name = "Goal NameUpdate3"
    #response = requests.put('https://api.clickup.com/api/v2/goal/' +goal_id, headers=headers_variable, json={"name": "Goal NameUpdate3"})
    #assert response.status_code == response_status
    #assert response.json()['name'] == 'Goal NameUpdate1'
    #yield
    #response_for_get = requests.get('https://api.clickup.com/api/v2/goal/' + goal_id,headers=headers_variable)
    #assert response_for_get.status_code == response_status
    #assert response_for_get.json()['goal']['name'] == name
    #yield




