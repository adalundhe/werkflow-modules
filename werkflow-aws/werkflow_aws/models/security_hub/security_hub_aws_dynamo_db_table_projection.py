from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDynamoDbTableProjection(BaseModel):
    NonKeyAttributes: list[StrictStr] | None = None
    ProjectionType: StrictStr | None = None
