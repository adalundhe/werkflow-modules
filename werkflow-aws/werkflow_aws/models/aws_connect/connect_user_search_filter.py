from __future__ import annotations
from pydantic import BaseModel
from .connect_control_plane_tag_filter import ConnectControlPlaneTagFilter
from .connect_control_plane_user_attribute_filter import ConnectControlPlaneUserAttributeFilter


class ConnectUserSearchFilter(BaseModel):
    TagFilter: ConnectControlPlaneTagFilter | None = None
    UserAttributeFilter: ConnectControlPlaneUserAttributeFilter | None = None
