from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBGetResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
