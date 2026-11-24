from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ConnectionLogOptions(BaseModel):
    Enabled: StrictBool | None = None
    CloudwatchLogGroup: StrictStr | None = None
    CloudwatchLogStream: StrictStr | None = None
    IncludeAuthorizationPolicyContext: StrictBool | None = None
