from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_mitigation_action_params import IoTMitigationActionParams


class IoTUpdateMitigationActionRequest(BaseModel):
    actionName: StrictStr
    roleArn: StrictStr | None = None
    actionParams: IoTMitigationActionParams | None = None
