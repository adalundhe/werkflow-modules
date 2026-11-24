from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_mitigation_action_params import IoTMitigationActionParams


class IoTMitigationAction(BaseModel):
    name: StrictStr | None = None
    id: StrictStr | None = None
    roleArn: StrictStr | None = None
    actionParams: IoTMitigationActionParams | None = None
