from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_domain_description_type import CognitoIDPDomainDescriptionType


class CognitoIDPDescribeUserPoolDomainResponse(BaseModel):
    DomainDescription: CognitoIDPDomainDescriptionType | None = None
    ResponseMetadata: dict[str, Any] | None = None
