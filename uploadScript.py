import requests
import json

file_name = "helloWorld.py"
file_path = "helloWorld.py"
url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media"
access_token = "ya29.a0AfB_byCY2fMkMcXwKTFwqrROLT4vIrHqbbhgxkIV5n2CUIVaoB0QZ7KgbW2vptpM-1N2jGD37Oz_Pn7i4fkyodUXylciddOvyifRTayqcyrMDDYD5iORSyuBwa6mVsbBeSkJwVByU68oaOZrqrDV9nvI4ZfswpqZlXs-aCgYKAR0SARISFQGOcNnCNbJM-tIjSmGt9BvA_DLM2Q0171"
with open(file_path, "rb") as file:
    file_content = file.read()
payload = {}
headers = {
    'Authorization': f'Bearer {access_token}'
}
try:
    response = requests.post(url, headers=headers, data=file_content)
    if response.status_code == 200:
        response_data = response.json()
        file_id = response_data.get("id")
        update_url = f"https://www.googleapis.com/drive/v3/files/{file_id}"
        update_payload = {
            'name': file_name
        }
        update_data = json.dumps(update_payload)
        update_response = requests.patch(update_url, headers=headers, data=update_data)
        print(f"{file_name} uploaded successfully.")
    else:
        print(f"Error uploading file. Status Code: {response.status_code}")
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
