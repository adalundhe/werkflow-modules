from __future__ import annotations
from pydantic import BaseModel
from .awss3_logging_enabled_input import AWSS3LoggingEnabledInput


class AWSS3BucketLoggingStatus(BaseModel):
    LoggingEnabled: AWSS3LoggingEnabledInput | None = None
