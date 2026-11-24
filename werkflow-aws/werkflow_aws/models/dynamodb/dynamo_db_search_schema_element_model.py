from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBSearchSchemaElementModel(BaseModel):
    AttributeName: StrictStr | None = None
    SearchSchemaElementType: StrictStr | None = None
