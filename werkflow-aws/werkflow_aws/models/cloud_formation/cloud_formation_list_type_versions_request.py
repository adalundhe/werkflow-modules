from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListTypeVersionsRequest(BaseModel):
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    TypeName: StrictStr | None = None
    Arn: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    DeprecatedStatus: Literal['LIVE', 'DEPRECATED'] | None = None
    PublisherId: StrictStr | None = None
