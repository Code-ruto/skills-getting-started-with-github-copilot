from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_from_activity():
    initial_participants = list(activities["Chess Club"]["participants"])

    signup_response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "newstudent@mergington.edu"},
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        "/activities/Chess Club/signup",
        params={"email": "newstudent@mergington.edu"},
    )

    assert unregister_response.status_code == 200
    assert "newstudent@mergington.edu" not in activities["Chess Club"]["participants"]
    assert activities["Chess Club"]["participants"] == initial_participants
