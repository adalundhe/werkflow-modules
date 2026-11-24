from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_resource_server_type import CognitoIDPResourceServerType


class CognitoIDPListResourceServersResponse(BaseModel):
    ResourceServers: list[CognitoIDPResourceServerType] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
