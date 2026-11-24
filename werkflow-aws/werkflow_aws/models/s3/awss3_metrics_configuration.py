from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_metrics_filter import AWSS3MetricsFilter


class AWSS3MetricsConfiguration(BaseModel):
    Id: StrictStr | None = None
    Filter: AWSS3MetricsFilter | None = None
