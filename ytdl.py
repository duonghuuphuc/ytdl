# GitHub : https://github.com/duonghuuphuc/ytdl
# Version: 1.0_beta (17/Dec/2022 12:23 AM)
from urllib.parse import urlparse, parse_qs
import subprocess
import argparse


def get_youtube_video_id(url):
    """
    Returns <video_id> extracting from a given YouTube URL

    :param url: URL of YouTube video
    """

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url

    query = urlparse(url)

    if "youtube" in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif "youtu.be" in query.hostname:
        return query.path[1:]
    else:
        raise ValueError


if __name__ == '__main__':
    # Define parser
    parser = argparse.ArgumentParser(description="A wrapper of yt-dlp toolkit to download YouTube video. "
                                                 "Version-1 of this program downloads video-and-audio in best available quality. "
                                                 "It also support download the video's subtitle if available.")
    parser.add_argument(dest="youtube_url", help="A valid YouTube URL")
    parser.add_argument('--sub', '--s', dest='write_sub', required=False, action="store_true", help="Set True if you want to download the video's subtitle")
    args = parser.parse_args()

    # Initialize arguments
    video_id = get_youtube_video_id(args.youtube_url)
    write_sub = args.write_sub

    # Download video
    video_url = "https://www.youtube.com/watch?v=" + video_id
    if write_sub:
        subprocess.call(["yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", "--write-sub", video_url])
    else:
        subprocess.call(["yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", video_url])
