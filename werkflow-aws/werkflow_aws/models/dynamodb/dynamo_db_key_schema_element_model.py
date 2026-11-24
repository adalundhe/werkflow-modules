from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBKeySchemaElementModel(BaseModel):
    AttributeName: StrictStr | None = None
    KeyType: StrictStr | None = None
