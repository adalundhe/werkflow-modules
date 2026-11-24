from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class AWSS3PutBucketEncryptionResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
