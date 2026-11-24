from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListTypeRegistrationsRequest(BaseModel):
    Type: Literal['RESOURCE', 'MODULE', 'HOOK'] | None = None
    TypeName: StrictStr | None = None
    TypeArn: StrictStr | None = None
    RegistrationStatusFilter: Literal['COMPLETE', 'IN_PROGRESS', 'FAILED'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
