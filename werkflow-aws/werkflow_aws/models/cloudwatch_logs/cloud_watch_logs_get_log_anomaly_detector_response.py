from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchLogsGetLogAnomalyDetectorResponse(BaseModel):
    detectorName: StrictStr | None = None
    logGroupArnList: list[StrictStr] | None = None
    evaluationFrequency: StrictStr | None = None
    filterPattern: StrictStr | None = None
    anomalyDetectorStatus: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
    creationTimeStamp: StrictInt | None = None
    lastModifiedTimeStamp: StrictInt | None = None
    anomalyVisibilityTime: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
