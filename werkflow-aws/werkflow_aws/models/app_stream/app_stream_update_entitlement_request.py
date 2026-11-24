from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_entitlement_attribute import AppStreamEntitlementAttribute


class AppStreamUpdateEntitlementRequest(BaseModel):
    Name: StrictStr
    StackName: StrictStr
    Description: StrictStr | None = None
    AppVisibility: Literal['ALL', 'ASSOCIATED'] | None = None
    Attributes: list[AppStreamEntitlementAttribute] | None = None
