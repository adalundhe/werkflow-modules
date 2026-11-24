from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_cors_rule import AWSS3CORSRule


class AWSS3GetBucketCorsResponse(BaseModel):
    CORSRules: list[AWSS3CORSRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
