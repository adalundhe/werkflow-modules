from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_public_access_block_configuration import AWSS3PublicAccessBlockConfiguration


class AWSS3GetPublicAccessBlockResponse(BaseModel):
    PublicAccessBlockConfiguration: AWSS3PublicAccessBlockConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
