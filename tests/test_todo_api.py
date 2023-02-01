import requests
import pytest
import uuid


ENDPOINT = "https://todo.pixegami.io/"


# response = requests.get(ENDPOINT)
# print(response)

# data = response.json()
# print(data)

# status_code = response.status_code
# print(status_code)

def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload=payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    task_id = data["task"]["task_id"]

    get_task_response = get_task(task_id=task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    create_payload = new_task_payload()
    create_task_response = create_task(create_payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    new_payload = {
        "task_id": task_id,
        "user_id": create_payload["user_id"],
        "content": "my updated content",
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    assert task_id == update_task_response.json()["updated_task_id"]
    # print(update_task_response.json())

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

@pytest.mark.list_tasks
def test_can_list_tasks():
    n = 3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
    pass

    list_tasks_response = list_tasks(payload["user_id"])
    assert list_tasks_response.status_code == 200
    list_tasks_data = list_tasks_response.json()

    tasks = list_tasks_data["tasks"]
    assert len(tasks) == n

@pytest.mark.delete_task
def test_can_delete_task():
    create_task_payload = new_task_payload()
    create_task_response = create_task(create_task_payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200
    assert delete_task_response.json()["deleted_task_id"] == task_id

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
    assert get_task_response.json()["detail"] == f"Task {task_id} not found"


def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"delete-task/{task_id}")

def new_task_payload(
    content=f"test content {uuid.uuid4().hex}",
    user_id=f"test_user_{uuid.uuid4().hex}",
    is_done=False
    ):
    return {
        "content": content,
        "user_id": user_id,
        "is_done": is_done,
    }