from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_entitled_application import AppStreamEntitledApplication


class AppStreamListEntitledApplicationsResponse(BaseModel):
    EntitledApplications: list[AppStreamEntitledApplication] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
