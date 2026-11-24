from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .swf_activity_type_configuration import SWFActivityTypeConfiguration
from .swf_activity_type_info import SWFActivityTypeInfo


class SWFDescribeActivityTypeResponse(BaseModel):
    typeInfo: SWFActivityTypeInfo | None = None
    configuration: SWFActivityTypeConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
