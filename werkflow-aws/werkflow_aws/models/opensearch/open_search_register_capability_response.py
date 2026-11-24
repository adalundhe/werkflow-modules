from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_capability_base_response_config import OpenSearchCapabilityBaseResponseConfig


class OpenSearchRegisterCapabilityResponse(BaseModel):
    capabilityName: StrictStr | None = None
    applicationId: StrictStr | None = None
    status: StrictStr | None = None
    capabilityConfig: OpenSearchCapabilityBaseResponseConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
