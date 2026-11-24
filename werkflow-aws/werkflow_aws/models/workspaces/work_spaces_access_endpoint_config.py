from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_access_endpoint import WorkSpacesAccessEndpoint


class WorkSpacesAccessEndpointConfig(BaseModel):
    AccessEndpoints: list[WorkSpacesAccessEndpoint] | None = None
    InternetFallbackProtocols: list[StrictStr] | None = None
