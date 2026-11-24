from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_predefined_attribute_configuration import ConnectPredefinedAttributeConfiguration
from .connect_predefined_attribute_values import ConnectPredefinedAttributeValues


class ConnectPredefinedAttribute(BaseModel):
    Name: StrictStr | None = None
    Values: ConnectPredefinedAttributeValues | None = None
    Purposes: list[StrictStr] | None = None
    AttributeConfiguration: ConnectPredefinedAttributeConfiguration | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LastModifiedRegion: StrictStr | None = None
