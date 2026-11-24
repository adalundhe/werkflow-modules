from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationDeactivateTypeRequest(BaseModel):
    TypeName: StrictStr | None = None
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    Arn: StrictStr | None = None
