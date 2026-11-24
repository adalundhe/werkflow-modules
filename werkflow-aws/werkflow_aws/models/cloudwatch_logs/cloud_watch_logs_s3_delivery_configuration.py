from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsS3DeliveryConfiguration(BaseModel):
    suffixPath: StrictStr | None = None
    enableHiveCompatiblePath: StrictBool | None = None
