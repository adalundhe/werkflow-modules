from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_analytics_configuration import AWSS3AnalyticsConfiguration


class AWSS3GetBucketAnalyticsConfigurationResponse(BaseModel):
    AnalyticsConfiguration: AWSS3AnalyticsConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
