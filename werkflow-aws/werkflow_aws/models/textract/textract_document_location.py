from __future__ import annotations
from pydantic import BaseModel
from .textract_s3_object import TextractS3Object


class TextractDocumentLocation(BaseModel):
    S3Object: TextractS3Object | None = None
