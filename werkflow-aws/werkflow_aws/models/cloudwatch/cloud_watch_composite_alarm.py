from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from typing import Literal


class CloudWatchCompositeAlarm(BaseModel):
    ActionsEnabled: StrictBool | None = None
    AlarmActions: list[StrictStr] | None = None
    AlarmArn: StrictStr | None = None
    AlarmConfigurationUpdatedTimestamp: datetime.datetime | None = None
    AlarmDescription: StrictStr | None = None
    AlarmName: StrictStr | None = None
    AlarmRule: StrictStr | None = None
    InsufficientDataActions: list[StrictStr] | None = None
    OKActions: list[StrictStr] | None = None
    StateReason: StrictStr | None = None
    StateReasonData: StrictStr | None = None
    StateUpdatedTimestamp: datetime.datetime | None = None
    StateValue: Literal['OK', 'ALARM', 'INSUFFICIENT_DATA'] | None = None
