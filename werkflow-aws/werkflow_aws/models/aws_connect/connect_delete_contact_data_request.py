from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDeleteContactDataRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    ContactFields: list[Literal['CUSTOMER_ENDPOINT', 'ADDITIONAL_EMAIL_RECIPIENTS', 'EMAIL_SUBJECT']]
