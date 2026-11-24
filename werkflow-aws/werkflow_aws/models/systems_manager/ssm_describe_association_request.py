from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDescribeAssociationRequest(BaseModel):
    Name: StrictStr | None = None
    InstanceId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
