from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cognito_idp_resource_server_type import CognitoIDPResourceServerType


class CognitoIDPDescribeResourceServerResponse(BaseModel):
    ResourceServer: CognitoIDPResourceServerType | None = None
    ResponseMetadata: dict[str, Any] | None = None
