from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .awss3_metrics_configuration import AWSS3MetricsConfiguration


class AWSS3GetBucketMetricsConfigurationResponse(BaseModel):
    MetricsConfiguration: AWSS3MetricsConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
