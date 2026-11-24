from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_terms_description_type import CognitoIDPTermsDescriptionType


class CognitoIDPListTermsResponse(BaseModel):
    Terms: list[CognitoIDPTermsDescriptionType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
