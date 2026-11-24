from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationTestTypeRequest(BaseModel):
    Arn: StrictStr | None = None
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    TypeName: StrictStr | None = None
    VersionId: StrictStr | None = None
    LogDeliveryBucket: StrictStr | None = None
