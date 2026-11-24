from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DynamoDBPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    Policy: StrictStr
    ExpectedRevisionId: StrictStr | None = None
    ConfirmRemoveSelfResourceAccess: StrictBool | None = None
