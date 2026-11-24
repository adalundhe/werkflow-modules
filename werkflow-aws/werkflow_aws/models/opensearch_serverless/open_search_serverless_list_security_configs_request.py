from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchServerlessListSecurityConfigsRequest(BaseModel):
    type: Literal['saml', 'iamidentitycenter', 'iamfederation']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
