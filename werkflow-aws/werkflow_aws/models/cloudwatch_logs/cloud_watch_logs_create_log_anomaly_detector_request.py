from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsCreateLogAnomalyDetectorRequest(BaseModel):
    logGroupArnList: list[StrictStr]
    detectorName: StrictStr | None = None
    evaluationFrequency: Literal['ONE_MIN', 'FIVE_MIN', 'TEN_MIN', 'FIFTEEN_MIN', 'THIRTY_MIN', 'ONE_HOUR'] | None = None
    filterPattern: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
    anomalyVisibilityTime: StrictInt | None = None
    tags: dict[StrictStr, StrictStr] | None = None
