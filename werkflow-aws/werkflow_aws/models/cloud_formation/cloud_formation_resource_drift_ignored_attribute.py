from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationResourceDriftIgnoredAttribute(BaseModel):
    Path: StrictStr | None = None
    Reason: StrictStr | None = None
