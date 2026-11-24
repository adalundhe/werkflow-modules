from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTReplaceDefaultPolicyVersionParams(BaseModel):
    templateName: StrictStr | None = None
