from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_command import EMRCommand


class EMRListBootstrapActionsResponse(BaseModel):
    BootstrapActions: list[EMRCommand] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
