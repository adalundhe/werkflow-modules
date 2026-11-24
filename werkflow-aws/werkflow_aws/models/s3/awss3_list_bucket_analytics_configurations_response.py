from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .awss3_analytics_configuration import AWSS3AnalyticsConfiguration


class AWSS3ListBucketAnalyticsConfigurationsResponse(BaseModel):
    IsTruncated: StrictBool | None = None
    ContinuationToken: StrictStr | None = None
    NextContinuationToken: StrictStr | None = None
    AnalyticsConfigurationList: list[AWSS3AnalyticsConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
