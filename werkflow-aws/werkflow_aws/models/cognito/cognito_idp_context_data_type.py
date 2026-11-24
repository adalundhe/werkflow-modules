from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_http_header import CognitoIDPHttpHeader


class CognitoIDPContextDataType(BaseModel):
    IpAddress: StrictStr
    ServerName: StrictStr
    ServerPath: StrictStr
    HttpHeaders: list[CognitoIDPHttpHeader]
    EncodedData: StrictStr | None = None
