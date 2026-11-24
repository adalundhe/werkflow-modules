from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeSessionsRequest(BaseModel):
    StackName: StrictStr
    FleetName: StrictStr
    UserId: StrictStr | None = None
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
    AuthenticationType: Literal['API', 'SAML', 'USERPOOL', 'AWS_AD'] | None = None
    InstanceId: StrictStr | None = None
