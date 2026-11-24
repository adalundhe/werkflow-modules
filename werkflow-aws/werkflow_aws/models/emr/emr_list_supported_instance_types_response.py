from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_supported_instance_type import EMRSupportedInstanceType


class EMRListSupportedInstanceTypesResponse(BaseModel):
    SupportedInstanceTypes: list[EMRSupportedInstanceType] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
