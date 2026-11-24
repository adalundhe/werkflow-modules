from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListMitigationActionsRequest(BaseModel):
    actionType: Literal['UPDATE_DEVICE_CERTIFICATE', 'UPDATE_CA_CERTIFICATE', 'ADD_THINGS_TO_THING_GROUP', 'REPLACE_DEFAULT_POLICY_VERSION', 'ENABLE_IOT_LOGGING', 'PUBLISH_FINDING_TO_SNS'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
