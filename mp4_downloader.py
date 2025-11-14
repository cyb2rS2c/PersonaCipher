import yt_dlp

def download_youtube_video(url, download_path=".", video_quality="best"):
    ydl_opts = {
        'format': video_quality,
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'concurrent_fragments': 4, 
        'noprogress': True,  
        'quiet': True,  
        'merge_output_format': 'mp4', 
        'max_filesize': None,  
        'retry_sleep': 5,  
        'http_chunk_size': 1048576,  # 1MB chunks for faster download
        'external_downloader': 'aria2c',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage:
url = input("Enter the video URL: ")
download_path = input("Enter the download path (default is current directory): ") or "."
video_quality = input("Enter video quality ('best', 'worst', '720p', etc.): ") or "best"

download_youtube_video(url, download_path, video_quality)
