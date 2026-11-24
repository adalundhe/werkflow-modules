from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_capability_extended_response_config import OpenSearchCapabilityExtendedResponseConfig
from .open_search_capability_failure import OpenSearchCapabilityFailure


class OpenSearchGetCapabilityResponse(BaseModel):
    capabilityName: StrictStr | None = None
    applicationId: StrictStr | None = None
    status: StrictStr | None = None
    capabilityConfig: OpenSearchCapabilityExtendedResponseConfig | None = None
    failures: list[OpenSearchCapabilityFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
