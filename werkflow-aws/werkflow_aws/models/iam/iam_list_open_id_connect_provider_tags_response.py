from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_tag_model import IAMTagModel


class IAMListOpenIDConnectProviderTagsResponse(BaseModel):
    Tags: list[IAMTagModel] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
