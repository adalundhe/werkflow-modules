from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDisassociateOpsItemRelatedItemRequest(BaseModel):
    OpsItemId: StrictStr
    AssociationId: StrictStr
