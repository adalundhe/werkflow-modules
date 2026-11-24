from __future__ import annotations
from pydantic import BaseModel
from .x_ray_graph_link import XRayGraphLink
from .x_ray_service import XRayService


class XRayRetrievedService(BaseModel):
    Service: XRayService | None = None
    Links: list[XRayGraphLink] | None = None
