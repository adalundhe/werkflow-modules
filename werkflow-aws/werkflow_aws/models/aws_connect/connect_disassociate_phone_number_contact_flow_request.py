from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociatePhoneNumberContactFlowRequest(BaseModel):
    PhoneNumberId: StrictStr
    InstanceId: StrictStr
