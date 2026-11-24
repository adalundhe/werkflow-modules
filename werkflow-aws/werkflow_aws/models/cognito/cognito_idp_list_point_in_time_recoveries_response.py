from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_restoration_description_type import CognitoIDPRestorationDescriptionType


class CognitoIDPListPointInTimeRecoveriesResponse(BaseModel):
    Restorations: list[CognitoIDPRestorationDescriptionType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
