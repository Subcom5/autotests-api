import httpx


login_payload = {
    "email": "test1@mail.com",
    "password": "12345"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

accessToken_data = login_response_data["token"]["accessToken"]

headers = {"Authorization": f"Bearer {accessToken_data}"}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Response body: ", me_response.json())
print("Status Code: ", me_response.status_code)

