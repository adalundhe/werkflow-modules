from __future__ import annotations
from pydantic import BaseModel
from .connect_control_plane_tag_filter import ConnectControlPlaneTagFilter


class ConnectRoutingProfileSearchFilter(BaseModel):
    TagFilter: ConnectControlPlaneTagFilter | None = None
