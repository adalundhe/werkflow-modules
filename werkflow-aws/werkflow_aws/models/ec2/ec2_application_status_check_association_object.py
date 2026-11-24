from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ApplicationStatusCheckAssociationObject(BaseModel):
    ApplicationStatusCheckId: StrictStr | None = None
    AssociationType: StrictStr | None = None
    Key: StrictStr | None = None
    Value: StrictStr | None = None
