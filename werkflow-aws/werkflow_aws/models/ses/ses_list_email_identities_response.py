from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_identity_info import SESIdentityInfo


class SESListEmailIdentitiesResponse(BaseModel):
    EmailIdentities: list[SESIdentityInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
