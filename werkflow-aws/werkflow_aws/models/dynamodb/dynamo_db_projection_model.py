from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBProjectionModel(BaseModel):
    ProjectionType: StrictStr | None = None
    NonKeyAttributes: list[StrictStr] | None = None
