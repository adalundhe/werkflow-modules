from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_instance_type_details import OpenSearchInstanceTypeDetails


class OpenSearchListInstanceTypeDetailsResponse(BaseModel):
    InstanceTypeDetails: list[OpenSearchInstanceTypeDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
