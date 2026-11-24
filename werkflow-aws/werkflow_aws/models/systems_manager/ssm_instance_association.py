from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMInstanceAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    InstanceId: StrictStr | None = None
    Content: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
