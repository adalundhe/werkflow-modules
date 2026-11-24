from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsCreateApplicationPresignedUrlRequest(BaseModel):
    ApplicationName: StrictStr
    UrlType: Literal['FLINK_DASHBOARD_URL', 'ZEPPELIN_UI_URL']
    SessionExpirationDurationInSeconds: StrictInt | None = None
