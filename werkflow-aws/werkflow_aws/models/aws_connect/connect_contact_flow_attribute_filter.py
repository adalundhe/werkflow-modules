from __future__ import annotations
from pydantic import BaseModel
from .connect_contact_flow_attribute_and_condition import ConnectContactFlowAttributeAndCondition
from .connect_contact_flow_type_condition import ConnectContactFlowTypeCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectContactFlowAttributeFilter(BaseModel):
    OrConditions: list[ConnectContactFlowAttributeAndCondition] | None = None
    AndCondition: ConnectContactFlowAttributeAndCondition | None = None
    TagCondition: ConnectTagCondition | None = None
    ContactFlowTypeCondition: ConnectContactFlowTypeCondition | None = None
