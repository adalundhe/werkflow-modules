from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_contact_data_request import ConnectContactDataRequest


class ConnectBatchPutContactRequest(BaseModel):
    InstanceId: StrictStr
    ContactDataRequestList: list[ConnectContactDataRequest]
    ClientToken: StrictStr | None = None
