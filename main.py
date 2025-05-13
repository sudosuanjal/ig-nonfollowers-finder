import json

try:
    with open('followers.json', 'r') as followers_file:
        followers_data = json.load(followers_file)
    with open('following.json', 'r') as following_file:
        following_data = json.load(following_file)
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)

# Function to extract usernames from data
def extract_usernames(data):
    usernames = set()
    # Handle different possible structures
    if isinstance(data, dict):
        if 'string_list_data' in data:
            for item in data['string_list_data']:
                usernames.add(item['value'])
        elif 'relationships_following' in data:  # Alternative structure
            for entry in data['relationships_following']:
                for item in entry['string_list_data']:
                    usernames.add(item['value'])
    elif isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict) and 'string_list_data' in entry:
                for item in entry['string_list_data']:
                    usernames.add(item['value'])
    return usernames

# Function to extract non-followers with hrefs
def find_non_followers(following_data, followers_set):
    non_followers = []
    if isinstance(following_data, dict):
        if 'relationships_following' in following_data:
            following_data = following_data['relationships_following']
    if isinstance(following_data, list):
        for entry in following_data:
            if isinstance(entry, dict) and 'string_list_data' in entry:
                for item in entry['string_list_data']:
                    if item['value'] not in followers_set:
                        non_followers.append(item['href'])
    return non_followers

# Extract followers
followers = extract_usernames(followers_data)

# Find non-followers
non_followers = find_non_followers(following_data, followers)

# Create output data structure
output_data = {
    "non_followers": non_followers
}

# Save to new JSON file
try:
    with open('non_followers.json', 'w') as output_file:
        json.dump(output_data, output_file, indent=2)
    print(f"Found {len(non_followers)} accounts that don't follow you back.")
    print("Results saved to 'non_followers.json'")
except Exception as e:
    print(f"Error saving file: {e}")