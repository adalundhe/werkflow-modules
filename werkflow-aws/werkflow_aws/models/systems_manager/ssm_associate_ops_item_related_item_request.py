from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMAssociateOpsItemRelatedItemRequest(BaseModel):
    OpsItemId: StrictStr
    AssociationType: StrictStr
    ResourceType: StrictStr
    ResourceUri: StrictStr
