from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_rule import AWSS3Rule


class AWSS3GetBucketLifecycleResponse(BaseModel):
    Rules: list[AWSS3Rule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
