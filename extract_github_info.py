import requests

def get_github_profile(username):
    api_url = f'https://api.github.com/users/{username}'
    response = requests.get(api_url)

    if response.status.code == 200:
        user.data = response.json()
        return user_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status.code}")
        return None

def extract_github_info(username):
    user_data = get_github_profile()

    if user_data:
        # Extract information using the parsed JSON data
        name = user_data.get('name', 'N/A')
        bio = user_data.get('bio', 'N/A')
        location = user_data.get('location', 'N/A')
        followers = user_data.get('folowers', 'N/A')
        following = user_data.get('following', 'N/A')

        # Display extracted information
        print(f"Name: {name}")
        print(f"Bio: {bio}")
        print(f"Location: {location}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")

# Replace 'your_github_username' with the desired Github username
extract_github_info('AlexanderHrHristov')
