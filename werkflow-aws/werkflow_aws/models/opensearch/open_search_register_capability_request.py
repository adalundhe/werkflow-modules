from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_capability_base_request_config import OpenSearchCapabilityBaseRequestConfig


class OpenSearchRegisterCapabilityRequest(BaseModel):
    applicationId: StrictStr
    capabilityName: StrictStr
    capabilityConfig: OpenSearchCapabilityBaseRequestConfig
