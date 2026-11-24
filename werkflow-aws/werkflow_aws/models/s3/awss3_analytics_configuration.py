from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_analytics_filter import AWSS3AnalyticsFilter
from .awss3_storage_class_analysis import AWSS3StorageClassAnalysis


class AWSS3AnalyticsConfiguration(BaseModel):
    Id: StrictStr | None = None
    Filter: AWSS3AnalyticsFilter | None = None
    StorageClassAnalysis: AWSS3StorageClassAnalysis | None = None
