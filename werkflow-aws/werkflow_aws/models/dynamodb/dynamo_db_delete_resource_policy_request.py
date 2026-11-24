from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    ExpectedRevisionId: StrictStr | None = None
