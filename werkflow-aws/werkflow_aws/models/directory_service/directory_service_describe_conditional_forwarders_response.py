from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_conditional_forwarder import DirectoryServiceConditionalForwarder


class DirectoryServiceDescribeConditionalForwardersResponse(BaseModel):
    ConditionalForwarders: list[DirectoryServiceConditionalForwarder] | None = None
    ResponseMetadata: dict[str, Any] | None = None
