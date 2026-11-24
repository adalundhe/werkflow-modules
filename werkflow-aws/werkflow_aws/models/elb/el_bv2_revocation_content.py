from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ELBv2RevocationContent(BaseModel):
    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
    S3ObjectVersion: StrictStr | None = None
    RevocationType: Literal['CRL'] | None = None
