from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontFunctionAssociation(BaseModel):
    FunctionARN: StrictStr | None = None
    EventType: StrictStr | None = None
