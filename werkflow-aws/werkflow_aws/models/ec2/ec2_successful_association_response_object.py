from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2SuccessfulAssociationResponseObject(BaseModel):
    ApplicationStatusCheckId: StrictStr | None = None
    AssociationType: StrictStr | None = None
    AssociationValue: StrictStr | None = None
