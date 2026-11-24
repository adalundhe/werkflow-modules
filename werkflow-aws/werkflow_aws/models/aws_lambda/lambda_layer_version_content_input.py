from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class LambdaLayerVersionContentInput(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
    S3ObjectVersion: StrictStr | None = None
    S3ObjectStorageMode: Literal['COPY', 'REFERENCE'] | None = None
    ZipFile: StrictBytes | BinaryIO | StrictStr | None = None
