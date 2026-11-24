from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsCreateLogGroupRequest(BaseModel):
    logGroupName: StrictStr
    kmsKeyId: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    logGroupClass: Literal['STANDARD', 'INFREQUENT_ACCESS', 'DELIVERY', 'ESSENTIALS'] | None = None
    deletionProtectionEnabled: StrictBool | None = None
