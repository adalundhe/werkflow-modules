from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMOpsItemIdentity(BaseModel):
    Arn: StrictStr | None = None
