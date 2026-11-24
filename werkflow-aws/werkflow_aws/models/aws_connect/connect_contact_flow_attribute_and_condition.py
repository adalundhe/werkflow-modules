from __future__ import annotations
from pydantic import BaseModel
from .connect_contact_flow_type_condition import ConnectContactFlowTypeCondition
from .connect_tag_condition import ConnectTagCondition


class ConnectContactFlowAttributeAndCondition(BaseModel):
    TagConditions: list[ConnectTagCondition] | None = None
    ContactFlowTypeCondition: ConnectContactFlowTypeCondition | None = None
