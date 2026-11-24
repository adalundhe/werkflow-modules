from __future__ import annotations
from pydantic import BaseModel
from .rekognition_kinesis_video_stream import RekognitionKinesisVideoStream


class RekognitionStreamProcessorInput(BaseModel):
    KinesisVideoStream: RekognitionKinesisVideoStream | None = None
