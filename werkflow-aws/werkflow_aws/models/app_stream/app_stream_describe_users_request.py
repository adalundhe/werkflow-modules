from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeUsersRequest(BaseModel):
    AuthenticationType: Literal['API', 'SAML', 'USERPOOL', 'AWS_AD']
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
