from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_entitlement_attribute import AppStreamEntitlementAttribute


class AppStreamCreateEntitlementRequest(BaseModel):
    Name: StrictStr
    StackName: StrictStr
    AppVisibility: Literal['ALL', 'ASSOCIATED']
    Attributes: list[AppStreamEntitlementAttribute]
    Description: StrictStr | None = None
