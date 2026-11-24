from __future__ import annotations
from pydantic import BaseModel
from .timestream_query_sns_configuration import TimestreamQuerySnsConfiguration


class TimestreamQueryNotificationConfiguration(BaseModel):
    SnsConfiguration: TimestreamQuerySnsConfiguration | None = None
