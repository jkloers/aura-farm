from yt_import import yt_import

url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
import_dir = "video/imported"

if __name__ == "__main__":
    yt_import(url, import_dir)
    scene_detection()
