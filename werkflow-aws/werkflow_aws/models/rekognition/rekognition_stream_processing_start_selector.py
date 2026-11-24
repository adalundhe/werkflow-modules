from __future__ import annotations
from pydantic import BaseModel
from .rekognition_kinesis_video_stream_start_selector import RekognitionKinesisVideoStreamStartSelector


class RekognitionStreamProcessingStartSelector(BaseModel):
    KVSStreamStartSelector: RekognitionKinesisVideoStreamStartSelector | None = None
