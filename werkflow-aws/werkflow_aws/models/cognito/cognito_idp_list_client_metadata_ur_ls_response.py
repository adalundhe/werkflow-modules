from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cognito_idp_client_metadata_url_type import CognitoIDPClientMetadataURLType


class CognitoIDPListClientMetadataURLsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ClientMetadataURLs: list[CognitoIDPClientMetadataURLType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
