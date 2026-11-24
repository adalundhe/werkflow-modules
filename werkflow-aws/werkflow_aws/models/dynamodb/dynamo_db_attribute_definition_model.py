from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBAttributeDefinitionModel(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeType: StrictStr | None = None
