from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationDeregisterTypeRequest(BaseModel):
    Arn: StrictStr | None = None
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    TypeName: StrictStr | None = None
    VersionId: StrictStr | None = None
