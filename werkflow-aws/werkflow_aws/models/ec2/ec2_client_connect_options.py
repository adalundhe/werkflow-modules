from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ClientConnectOptions(BaseModel):
    Enabled: StrictBool | None = None
    LambdaFunctionArn: StrictStr | None = None
