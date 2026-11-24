from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_entitlement_attribute import AppStreamEntitlementAttribute


class AppStreamEntitlement(BaseModel):
    Name: StrictStr | None = None
    StackName: StrictStr | None = None
    Description: StrictStr | None = None
    AppVisibility: StrictStr | None = None
    Attributes: list[AppStreamEntitlementAttribute] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
