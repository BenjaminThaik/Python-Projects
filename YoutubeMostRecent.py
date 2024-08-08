'''
References: https://developers.google.com/youtube/v3/getting-started
'''

#Allows connection between YouTube Data API V3 (Google Cloud and Python)
from googleapiclient.discovery import build
# Replace with your API key
API_KEY = ""
# Special ID that differentiates Youtube Channels
CHANNEL_ID = ["UCBJycsmduvYEL83R_U4JriQ","UCOmcA3f_RrH6b9NmcNa4tdg","UCXuqSBlHAE6Xw-yeJA0Tunw"]
#Array to hold the most recent video for the given number of YouTube Channels
video_urls = []

''''
This function 
'''
def get_latest_videos(api_key, channel_id, max_results=1):
    # Uses the YouTube V3 API to make requests from the YouTube Data API
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Retrieves the uploads playlist ID
    request = youtube.channels().list(part='contentDetails', id=channel_id)
    response = request.execute()
    # Path taken is youtube#channel -> contentDetails -> relatedPlaylists -> uploads
    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieves the latest videos from the uploads playlist
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist_id,
        maxResults=max_results
    )
    response = request.execute()

    # Retrieves data and constructs a  live YouTube link to the most recent video from the given channel
    for item in response['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_urls.append(f'https://www.youtube.com/watch?v={video_id}')

    return video_urls

if __name__ == '__main__':
    for channel_id in CHANNEL_ID:
        latest_videos = get_latest_videos(API_KEY, channel_id)
    for video in latest_videos:
        print(video)