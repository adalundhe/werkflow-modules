from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_service_software_options import OpenSearchServiceSoftwareOptions


class OpenSearchStartServiceSoftwareUpdateResponse(BaseModel):
    ServiceSoftwareOptions: OpenSearchServiceSoftwareOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None
