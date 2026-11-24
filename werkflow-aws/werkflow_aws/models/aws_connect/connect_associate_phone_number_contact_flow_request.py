from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAssociatePhoneNumberContactFlowRequest(BaseModel):
    PhoneNumberId: StrictStr
    InstanceId: StrictStr
    ContactFlowId: StrictStr
