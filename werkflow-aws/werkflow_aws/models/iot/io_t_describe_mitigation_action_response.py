from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_mitigation_action_params import IoTMitigationActionParams


class IoTDescribeMitigationActionResponse(BaseModel):
    actionName: StrictStr | None = None
    actionType: StrictStr | None = None
    actionArn: StrictStr | None = None
    actionId: StrictStr | None = None
    roleArn: StrictStr | None = None
    actionParams: IoTMitigationActionParams | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
