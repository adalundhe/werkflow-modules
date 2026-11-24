from __future__ import annotations
from pydantic import BaseModel
from .connect_contact_flow_attribute_filter import ConnectContactFlowAttributeFilter
from .connect_control_plane_tag_filter import ConnectControlPlaneTagFilter


class ConnectContactFlowSearchFilter(BaseModel):
    TagFilter: ConnectControlPlaneTagFilter | None = None
    FlowAttributeFilter: ConnectContactFlowAttributeFilter | None = None
