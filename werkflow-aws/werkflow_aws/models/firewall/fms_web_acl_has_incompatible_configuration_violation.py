from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSWebACLHasIncompatibleConfigurationViolation(BaseModel):
    WebACLArn: StrictStr | None = None
    Description: StrictStr | None = None
