from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_analytics_configuration import AWSS3AnalyticsConfiguration


class AWSS3PutBucketAnalyticsConfigurationRequest(BaseModel):
    Bucket: StrictStr
    Id: StrictStr
    AnalyticsConfiguration: AWSS3AnalyticsConfiguration
    ExpectedBucketOwner: StrictStr | None = None
