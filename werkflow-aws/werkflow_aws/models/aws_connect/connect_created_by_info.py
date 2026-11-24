from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreatedByInfo(BaseModel):
    ConnectUserArn: StrictStr | None = None
    AWSIdentityArn: StrictStr | None = None
