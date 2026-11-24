from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_abac_status import AWSS3AbacStatus


class AWSS3GetBucketAbacResponse(BaseModel):
    AbacStatus: AWSS3AbacStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
