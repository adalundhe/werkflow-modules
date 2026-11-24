from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetOpsItemRequest(BaseModel):
    OpsItemId: StrictStr
    OpsItemArn: StrictStr | None = None
