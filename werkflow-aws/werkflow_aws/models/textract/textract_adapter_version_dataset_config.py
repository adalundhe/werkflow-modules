from __future__ import annotations
from pydantic import BaseModel
from .textract_s3_object import TextractS3Object


class TextractAdapterVersionDatasetConfig(BaseModel):
    ManifestS3Object: TextractS3Object | None = None
