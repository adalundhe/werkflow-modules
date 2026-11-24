from __future__ import annotations
from pydantic import BaseModel
from .connect_control_plane_attribute_filter import ConnectControlPlaneAttributeFilter


class ConnectWorkspaceAssociationSearchFilter(BaseModel):
    AttributeFilter: ConnectControlPlaneAttributeFilter | None = None
