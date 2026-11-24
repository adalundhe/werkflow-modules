from __future__ import annotations
from pydantic import BaseModel
from .rekognition_kinesis_data_stream import RekognitionKinesisDataStream
from .rekognition_s3_destination import RekognitionS3Destination


class RekognitionStreamProcessorOutput(BaseModel):
    KinesisDataStream: RekognitionKinesisDataStream | None = None
    S3Destination: RekognitionS3Destination | None = None
