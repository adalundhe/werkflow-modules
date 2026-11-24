from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDeleteAssociationRequest(BaseModel):
    Name: StrictStr | None = None
    InstanceId: StrictStr | None = None
    AssociationId: StrictStr | None = None
