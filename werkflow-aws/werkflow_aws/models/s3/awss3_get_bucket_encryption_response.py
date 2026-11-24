from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_server_side_encryption_configuration import AWSS3ServerSideEncryptionConfiguration


class AWSS3GetBucketEncryptionResponse(BaseModel):
    ServerSideEncryptionConfiguration: AWSS3ServerSideEncryptionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
