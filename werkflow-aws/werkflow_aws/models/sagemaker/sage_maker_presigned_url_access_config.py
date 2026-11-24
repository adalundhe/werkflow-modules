from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SageMakerPresignedUrlAccessConfig(BaseModel):
    AcceptEula: StrictBool | None = None
    ExpectedS3Url: StrictStr | None = None
