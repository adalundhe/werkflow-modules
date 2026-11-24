from __future__ import annotations
from pydantic import BaseModel
from .io_t_explicit_deny import IoTExplicitDeny
from .io_t_implicit_deny import IoTImplicitDeny


class IoTDenied(BaseModel):
    implicitDeny: IoTImplicitDeny | None = None
    explicitDeny: IoTExplicitDeny | None = None
