import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Arrange-Act-Assert pattern for GET /activities

def test_get_activities():
    # Arrange: テスト用の初期状態（特に準備不要、インメモリDB初期状態）
    # Act: GETリクエストを送信
    response = client.get("/activities")
    # Assert: レスポンス内容とステータスコードを検証
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Arrange-Act-Assert pattern for POST /activities/{activity_name}/signup

def test_signup_activity():
    # Arrange: テスト用データ
    activity_name = "hiking"
    email = "test@example.com"
    # Act: POSTリクエストを送信
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert: レスポンス内容とステータスコードを検証
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up for {activity_name}"

# Arrange-Act-Assert pattern for invalid signup (missing email)

def test_signup_activity_missing_email():
    # Arrange: テスト用データ
    activity_name = "hiking"
    # Act: POSTリクエスト（emailなし）
    response = client.post(f"/activities/{activity_name}/signup")
    # Assert: 422 Unprocessable Entity
    assert response.status_code == 422
