from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTimeSeriesForecastingSettings(BaseModel):
    Status: StrictStr | None = None
    AmazonForecastRoleArn: StrictStr | None = None
