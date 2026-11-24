from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_ownership_controls import AWSS3OwnershipControls


class AWSS3GetBucketOwnershipControlsResponse(BaseModel):
    OwnershipControls: AWSS3OwnershipControls | None = None
    ResponseMetadata: dict[str, Any] | None = None
