from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMParameterInlinePolicy(BaseModel):
    PolicyText: StrictStr | None = None
    PolicyType: StrictStr | None = None
    PolicyStatus: StrictStr | None = None
