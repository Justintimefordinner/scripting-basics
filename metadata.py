import eyed3


def trackNumber(filepath: str):
    """
    Retrieves the track number from the metadata of an audio file.

    Args:
        filepath (str): The full path of the audio file.

    Returns:
        int: The track number of the audio file.

    Raises:
        FileNotFoundError: If the audio file is not found at the specified path.

    """
    file = eyed3.load(filepath)
    return file.tag.track_num[0]

def trackTitle(filepath: str):
    """
    Retrieves the title of the track from the metadata of an audio file.

    Args:
        filepath (str): The full path of the audio file.

    Returns:
        str: The title of the audio file.

    Raises:
        FileNotFoundError: If the audio file is not found at the specified path.

    """
    file = eyed3.load(filepath)
    return file.tag.title
