from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_input_predefined_attribute_configuration import ConnectInputPredefinedAttributeConfiguration
from .connect_predefined_attribute_values import ConnectPredefinedAttributeValues


class ConnectCreatePredefinedAttributeRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    Values: ConnectPredefinedAttributeValues | None = None
    Purposes: list[StrictStr] | None = None
    AttributeConfiguration: ConnectInputPredefinedAttributeConfiguration | None = None
