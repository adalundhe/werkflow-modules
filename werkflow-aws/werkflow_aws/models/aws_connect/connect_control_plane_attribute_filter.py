from __future__ import annotations
from pydantic import BaseModel
from .connect_common_attribute_and_condition import ConnectCommonAttributeAndCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectControlPlaneAttributeFilter(BaseModel):
    OrConditions: list[ConnectCommonAttributeAndCondition] | None = None
    AndCondition: ConnectCommonAttributeAndCondition | None = None
    TagCondition: ConnectTagCondition | None = None
