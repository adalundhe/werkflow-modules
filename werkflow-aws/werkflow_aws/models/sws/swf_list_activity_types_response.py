from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .swf_activity_type_info import SWFActivityTypeInfo


class SWFListActivityTypesResponse(BaseModel):
    typeInfos: list[SWFActivityTypeInfo] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
