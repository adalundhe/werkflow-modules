from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_mitigation_action_params import IoTMitigationActionParams
from .io_t_tag import IoTTag


class IoTCreateMitigationActionRequest(BaseModel):
    actionName: StrictStr
    roleArn: StrictStr
    actionParams: IoTMitigationActionParams
    tags: list[IoTTag] | None = None
