from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeTypeRequest(BaseModel):
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    TypeName: StrictStr | None = None
    Arn: StrictStr | None = None
    VersionId: StrictStr | None = None
    PublisherId: StrictStr | None = None
    PublicVersionNumber: StrictStr | None = None
