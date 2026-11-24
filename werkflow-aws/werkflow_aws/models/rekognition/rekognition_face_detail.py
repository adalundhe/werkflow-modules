from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_age_range import RekognitionAgeRange
from .rekognition_beard import RekognitionBeard
from .rekognition_bounding_box import RekognitionBoundingBox
from .rekognition_emotion import RekognitionEmotion
from .rekognition_eye_direction import RekognitionEyeDirection
from .rekognition_eye_open import RekognitionEyeOpen
from .rekognition_eyeglasses import RekognitionEyeglasses
from .rekognition_face_occluded import RekognitionFaceOccluded
from .rekognition_gender import RekognitionGender
from .rekognition_image_quality import RekognitionImageQuality
from .rekognition_landmark import RekognitionLandmark
from .rekognition_mouth_open import RekognitionMouthOpen
from .rekognition_mustache import RekognitionMustache
from .rekognition_pose import RekognitionPose
from .rekognition_smile import RekognitionSmile
from .rekognition_sunglasses import RekognitionSunglasses


class RekognitionFaceDetail(BaseModel):
    BoundingBox: RekognitionBoundingBox | None = None
    AgeRange: RekognitionAgeRange | None = None
    Smile: RekognitionSmile | None = None
    Eyeglasses: RekognitionEyeglasses | None = None
    Sunglasses: RekognitionSunglasses | None = None
    Gender: RekognitionGender | None = None
    Beard: RekognitionBeard | None = None
    Mustache: RekognitionMustache | None = None
    EyesOpen: RekognitionEyeOpen | None = None
    MouthOpen: RekognitionMouthOpen | None = None
    Emotions: list[RekognitionEmotion] | None = None
    Landmarks: list[RekognitionLandmark] | None = None
    Pose: RekognitionPose | None = None
    Quality: RekognitionImageQuality | None = None
    Confidence: StrictFloat | StrictInt | None = None
    FaceOccluded: RekognitionFaceOccluded | None = None
    EyeDirection: RekognitionEyeDirection | None = None
