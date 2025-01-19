import time
import httpx
import pandas as pd

# Base URL and endpoint for the Reddit API
base_url = 'https://www.reddit.com'
endpoint = '/r/legaladviceofftopic/'
category = ''

url = base_url + endpoint + category + ".json"
after_post_id = None  # For pagination

dataset = []  # To store the filtered data (title, selftext, upvote_ratio)

# Fetch 5 pages of data
for _ in range(15):
    # Set parameters for the request
    params = {
        'limit': 100,  # Maximum posts per request
        't': 'year',   # Time filter (e.g., posts from the last year)
    }

    # Add 'after' parameter if it's not None (for pagination)
    if after_post_id:
        params['after'] = after_post_id

    # Make the request to Reddit
    response = httpx.get(url, params=params, headers={'User-Agent': 'Mozilla/5.0'})

    # Print the URL being fetched
    print(f'Fetching: "{response.url}"....')
 
    # Check for a successful response
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    # Parse the JSON response
    try:
        json_data = response.json()
    except ValueError:
        raise Exception("Invalid JSON response")

    # Extract posts' data and filter for useful fields
    for rec in json_data['data']['children']:
        post_data = rec['data']
        filtered_data = {
            'title': post_data.get('title', 'N/A'),
            'selftext': post_data.get('selftext', 'N/A'),
            'upvote_ratio': post_data.get('upvote_ratio', 'N/A')
        }
        dataset.append(filtered_data)

    # Update the pagination token for the next request
    after_post_id = json_data['data']['after']

    # Stop if there are no more posts to fetch
    if after_post_id is None:
        break

    # Be polite and wait a bit before the next request
    time.sleep(0.5)

# Convert the dataset to a DataFrame
df = pd.DataFrame(dataset)

# Write the DataFrame to an Excel file
output_file = 'reddit_legal_advice_OffTopic.xlsx'
df.to_excel(output_file, index=False)

print(f"Data has been written to {output_file}")
