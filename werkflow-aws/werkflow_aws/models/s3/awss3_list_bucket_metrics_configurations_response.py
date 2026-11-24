from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_metrics_configuration import AWSS3MetricsConfiguration


class AWSS3ListBucketMetricsConfigurationsResponse(BaseModel):
    IsTruncated: StrictBool | None = None
    ContinuationToken: StrictStr | None = None
    NextContinuationToken: StrictStr | None = None
    MetricsConfigurationList: list[AWSS3MetricsConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
