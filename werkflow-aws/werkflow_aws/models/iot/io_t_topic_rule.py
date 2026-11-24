from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_action import IoTAction


class IoTTopicRule(BaseModel):
    ruleName: StrictStr | None = None
    sql: StrictStr | None = None
    description: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    actions: list[IoTAction] | None = None
    ruleDisabled: StrictBool | None = None
    awsIotSqlVersion: StrictStr | None = None
    errorAction: IoTAction | None = None
