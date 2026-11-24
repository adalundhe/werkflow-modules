from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .iam_tag_model import IAMTagModel


class IAMCreateOpenIDConnectProviderResponse(BaseModel):
    OpenIDConnectProviderArn: StrictStr | None = None
    Tags: list[IAMTagModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
