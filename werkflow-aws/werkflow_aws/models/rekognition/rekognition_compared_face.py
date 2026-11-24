from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_emotion import RekognitionEmotion
from .rekognition_image_quality import RekognitionImageQuality
from .rekognition_landmark import RekognitionLandmark
from .rekognition_pose import RekognitionPose
from .rekognition_smile import RekognitionSmile


class RekognitionComparedFace(BaseModel):
    BoundingBox: RekognitionBoundingBox | None = None
    Confidence: StrictFloat | StrictInt | None = None
    Landmarks: list[RekognitionLandmark] | None = None
    Pose: RekognitionPose | None = None
    Quality: RekognitionImageQuality | None = None
    Emotions: list[RekognitionEmotion] | None = None
    Smile: RekognitionSmile | None = None
