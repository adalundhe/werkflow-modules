from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_terms_type import CognitoIDPTermsType


class CognitoIDPDescribeTermsResponse(BaseModel):
    Terms: CognitoIDPTermsType | None = None
    ResponseMetadata: dict[str, Any] | None = None
