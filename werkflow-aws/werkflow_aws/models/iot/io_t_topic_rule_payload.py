from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_action import IoTAction


class IoTTopicRulePayload(BaseModel):
    sql: StrictStr
    actions: list[IoTAction]
    description: StrictStr | None = None
    ruleDisabled: StrictBool | None = None
    awsIotSqlVersion: StrictStr | None = None
    errorAction: IoTAction | None = None
