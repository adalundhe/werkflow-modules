from __future__ import annotations
from pydantic import BaseModel
from .connect_primary_attribute_value import ConnectPrimaryAttributeValue


class ConnectPrimaryAttributeAccessControlConfigurationItem(BaseModel):
    PrimaryAttributeValues: list[ConnectPrimaryAttributeValue] | None = None
