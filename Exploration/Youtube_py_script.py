from googleapiclient.discovery import build
import csv

# Set up the API client
api_key = 'AIzaSyAicrjLt18EeS8_psF__UJZhyBqSgokPiU'
youtube = build('youtube', 'v3', developerKey=api_key)

# Set the video ID
video_id = 'HuMxQzX0uso'

# Get the comments
results = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    textFormat='plainText'
).execute()

# Open the CSV file for writing
with open('comments.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['comment_id', 'author', 'text', 'published_at'])

    # Write the comments to the CSV file
    for item in results['items']:
        comment = item['snippet']['topLevelComment']
        comment_id = comment['id']
        author = comment['snippet']['authorDisplayName']
        text = comment['snippet']['textDisplay']
        published_at = comment['snippet']['publishedAt']
        writer.writerow([comment_id, author, text, published_at])