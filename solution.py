import os
import csv
import metadata

def solution():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Set the relative path to the directory containing the files
    path = os.path.join(current_dir, "TMA")

    # Set the relative path to the tracklist.csv file
    csv_path = os.path.join(current_dir, "tracklist.csv")

    # Read the tracklist.csv file
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        tracklist = list(csv_reader)

    # Rename the files
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(path, filename)
            track_number = metadata.trackNumber(mp3_path)
            for track in tracklist:
                if track["track_number"] == track_number:
                    new_filename = f"{track['title']}.mp3"
                    new_mp3_path = os.path.join(path, new_filename)
                    os.rename(mp3_path, new_mp3_path)
                    break
