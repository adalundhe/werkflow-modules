from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationPublishTypeRequest(BaseModel):
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    Arn: StrictStr | None = None
    TypeName: StrictStr | None = None
    PublicVersionNumber: StrictStr | None = None
