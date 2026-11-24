from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBVectorAttributeDefinition(BaseModel):
    AttributeName: StrictStr
