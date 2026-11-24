from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_query_sns_configuration import TimestreamQuerySnsConfiguration


class TimestreamQueryAccountSettingsNotificationConfiguration(BaseModel):
    SnsConfiguration: TimestreamQuerySnsConfiguration | None = None
    RoleArn: StrictStr | None = None
