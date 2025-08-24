from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from scenedetect.scene_manager import save_images


def detect_scenes(video_path, output_dir='scenes', threshold=27.0):
    """
    Detects scenes in a video and saves thumbnails for each scene.
    Args:
        video_path (str): Path to the video file.
        output_dir (str): Directory to save scene thumbnails.
        threshold (float): Sensitivity for scene detection.
    """
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list()
    print("Scènes détectées :")
    for i, scene in enumerate(scene_list):
        start_time = scene[0].get_timecode()
        end_time = scene[1].get_timecode()
        print(f"Scène {i+1}: {start_time} --> {end_time}")
    save_images(scene_list, video_manager, num_images=1, output_dir=output_dir, image_name_template='$SCENE_NUMBER')
