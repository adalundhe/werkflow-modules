from __future__ import annotations
from pydantic import BaseModel
from .awss3_s3_location import AWSS3S3Location


class AWSS3OutputLocation(BaseModel):
    S3: AWSS3S3Location | None = None
