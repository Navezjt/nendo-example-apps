import yt_dlp
import argparse
import subprocess
from moviepy.editor import VideoFileClip, AudioFileClip
from nendo import NendoConfig, Nendo


# TODO

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--yt-link",
        type=str,
        required=True,
        help="Youtube link to download for the remix.",
    )
    parser.add_argument(
        "-p", "--prompt", type=str, required=True, help="Prompt to use for the remix."
    )
    parser.add_argument(
        "-o",
        "--output-video-path",
        type=str,
        default="output.mp4",
        help="Output path for the remix.",
    )
    return parser.parse_args()


def main(yt_link: str, prompt: str, output_video_path: str):
    video_path = yt_download(yt_link, 30, output_path="video")
    audio_path = extract_audio(video_path, output_path="audio.mp3")
    remixed_audio_path = run_nendo_plugin_chain(audio_path, prompt)
    remix_video(video_path, remixed_audio_path, output_path=output_video_path)


if __name__ == "__main__":
    args = parse_args()
    main(
        yt_link=args.yt_link,
        prompt=args.prompt,
        output_video_path=args.output_video_path,
    )
