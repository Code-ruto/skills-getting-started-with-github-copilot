from src.app import activities


def test_unregister_participant_from_activity(client):
    # Arrange
    email = "newstudent@mergington.edu"
    initial_participants = list(activities["Chess Club"]["participants"])

    # Act
    signup_response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email},
    )
    unregister_response = client.delete(
        "/activities/Chess Club/signup",
        params={"email": email},
    )

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert email not in activities["Chess Club"]["participants"]
    assert activities["Chess Club"]["participants"] == initial_participants
