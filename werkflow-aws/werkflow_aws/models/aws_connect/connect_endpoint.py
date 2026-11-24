from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectEndpoint(BaseModel):
    Type: Literal['TELEPHONE_NUMBER', 'VOIP', 'CONTACT_FLOW', 'CONNECT_PHONENUMBER_ARN', 'EMAIL_ADDRESS'] | None = None
    Address: StrictStr | None = None
