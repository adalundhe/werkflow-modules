from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_logging_enabled import AWSS3LoggingEnabled


class AWSS3GetBucketLoggingResponse(BaseModel):
    LoggingEnabled: AWSS3LoggingEnabled | None = None
    ResponseMetadata: dict[str, Any] | None = None
