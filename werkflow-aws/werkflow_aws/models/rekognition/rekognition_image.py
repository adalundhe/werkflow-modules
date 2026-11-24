from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .rekognition_s3_object import RekognitionS3Object


class RekognitionImage(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Bytes: StrictBytes | BinaryIO | StrictStr | None = None
    S3Object: RekognitionS3Object | None = None
