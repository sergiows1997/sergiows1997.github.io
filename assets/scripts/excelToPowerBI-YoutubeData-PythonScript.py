import os
import pandas as pd
from googleapiclient.discovery import build

api_key = 'AIzaSyDW0A-KlkdTI_HEY0h8RbQNvN3IdKOFFx4'
youtube = build('youtube', 'v3', developerKey= api_key)

def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part='snippet, statistics',
        id=channel_id
    )
    response = request.execute()

    if response['items']:

        data = dict(channel_name=response['items'][0]['snippet']['title'],
                    total_subscribers=response['items'][0]['statistics']['subscriberCount'],
                    total_views=response['items'][0]['statistics']['viewCount'],
                    total_videos=response['items'][0]['statistics']['videoCount'],
        )

        return data
    else:
        return None 
    

# channel_id = "UC_aEa8K-EOJ3D6gOs7HcyNg" 
channel_id = "UCGlFOT4_wS3vVROtpYL6mgQ"
get_channel_stats(youtube, channel_id)


# Read CSV into dataframe 
df = pd.read_csv("excelToPowerBI/youtube_data_files/youtube_data_peru.csv")



# Extract channel IDs and remove potential duplicates
channel_ids = df['NAME'].str.split('@').str[-1].unique()


# Initialize a list to keep track of channel stats
channel_stats = []


# Loop over the channel IDs and get stats for each
for channel_id in channel_ids:
    stats = get_channel_stats(youtube, channel_id)
    if stats is not None:
        channel_stats.append(stats)



# Convert the list of stats to a df
stats_df = pd.DataFrame(channel_stats)


df.reset_index(drop=True, inplace=True)
stats_df.reset_index(drop=True, inplace=True)


# Concatenate the dataframes horizontally
combined_df = pd.concat([df, stats_df], axis=1)


# Drop the 'channel_name' column from stats_df (since 'NOMBRE' already exists)
# combined_df.drop('channel_name', axis=1, inplace=True)


# Save the merged dataframe back into a CSV file
combined_df.to_csv('excelToPowerBI/youtube_data_files/updated_youtube_data_peru.csv', index=False)


combined_df.head(10)