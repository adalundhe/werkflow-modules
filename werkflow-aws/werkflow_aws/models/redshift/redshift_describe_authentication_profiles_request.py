from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDescribeAuthenticationProfilesRequest(BaseModel):
    AuthenticationProfileName: StrictStr | None = None
