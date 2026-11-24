from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_tag_info_for_resource import WAFv2TagInfoForResource


class WAFv2ListTagsForResourceResponse(BaseModel):
    NextMarker: StrictStr | None = None
    TagInfoForResource: WAFv2TagInfoForResource | None = None
    ResponseMetadata: dict[str, Any] | None = None
