from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeUserStackAssociationsRequest(BaseModel):
    StackName: StrictStr | None = None
    UserName: StrictStr | None = None
    AuthenticationType: Literal['API', 'SAML', 'USERPOOL', 'AWS_AD'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
