from __future__ import annotations
from pydantic import BaseModel
from .connect_invisible_field_info import ConnectInvisibleFieldInfo
from .connect_read_only_field_info import ConnectReadOnlyFieldInfo
from .connect_required_field_info import ConnectRequiredFieldInfo


class ConnectTaskTemplateConstraints(BaseModel):
    RequiredFields: list[ConnectRequiredFieldInfo] | None = None
    ReadOnlyFields: list[ConnectReadOnlyFieldInfo] | None = None
    InvisibleFields: list[ConnectInvisibleFieldInfo] | None = None
