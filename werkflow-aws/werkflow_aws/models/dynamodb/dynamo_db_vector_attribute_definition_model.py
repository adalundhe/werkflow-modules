from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBVectorAttributeDefinitionModel(BaseModel):
    AttributeName: StrictStr | None = None
