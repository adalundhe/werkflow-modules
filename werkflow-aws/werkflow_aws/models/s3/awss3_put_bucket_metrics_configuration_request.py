from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_metrics_configuration import AWSS3MetricsConfiguration


class AWSS3PutBucketMetricsConfigurationRequest(BaseModel):
    Bucket: StrictStr
    Id: StrictStr
    MetricsConfiguration: AWSS3MetricsConfiguration
    ExpectedBucketOwner: StrictStr | None = None
