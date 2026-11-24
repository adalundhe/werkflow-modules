from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMInlinePolicy(BaseModel):
    PolicyName: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
