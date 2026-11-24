from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_listener_attribute import ELBv2ListenerAttribute


class ELBv2ModifyListenerAttributesRequest(BaseModel):
    ListenerArn: StrictStr
    Attributes: list[ELBv2ListenerAttribute]
