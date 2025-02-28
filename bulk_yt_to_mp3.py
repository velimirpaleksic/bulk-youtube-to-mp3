import yt_dlp
import os

def download_video_as_mp3(video_url):
    try:
        output_template = "%(title)s.%(ext)s"

        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "outtmpl": output_template,
            "extractor_args": {"youtube": {"player_client": "android"}},
        }
        
        print(f"[*] Downloading video: {video_url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("[+] Download complete")
    except Exception as e:
        print(f"[-] Error: {e}")

def download_bulk_videos(input_file):
    if not os.path.exists(input_file):
        print(f"[-] Error: The file '{input_file}' does not exist.")
        return
    
    with open(input_file, "r") as file:
        video_urls = file.readlines()

    for video_url in video_urls:
        video_url = video_url.strip()  # Remove any extra spaces or newlines
        if video_url:
            download_video_as_mp3(video_url)

if __name__ == "__main__":
    input_file = "video_urls.txt"  # Replace with your text file containing URLs
    download_bulk_videos(input_file)