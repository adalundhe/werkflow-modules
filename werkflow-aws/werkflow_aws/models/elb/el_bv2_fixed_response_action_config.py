from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2FixedResponseActionConfig(BaseModel):
    MessageBody: StrictStr | None = None
    StatusCode: StrictStr | None = None
    ContentType: StrictStr | None = None
