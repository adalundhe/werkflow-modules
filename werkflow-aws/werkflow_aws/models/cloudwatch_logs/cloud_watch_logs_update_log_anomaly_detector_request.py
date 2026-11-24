from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CloudWatchLogsUpdateLogAnomalyDetectorRequest(BaseModel):
    anomalyDetectorArn: StrictStr
    enabled: StrictBool
    evaluationFrequency: Literal['ONE_MIN', 'FIVE_MIN', 'TEN_MIN', 'FIFTEEN_MIN', 'THIRTY_MIN', 'ONE_HOUR'] | None = None
    filterPattern: StrictStr | None = None
    anomalyVisibilityTime: StrictInt | None = None
