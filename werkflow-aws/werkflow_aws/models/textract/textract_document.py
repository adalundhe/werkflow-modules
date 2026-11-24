from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .textract_s3_object import TextractS3Object


class TextractDocument(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Bytes: StrictBytes | BinaryIO | StrictStr | None = None
    S3Object: TextractS3Object | None = None
