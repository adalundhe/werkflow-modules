from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDynamoDbTableAttributeDefinition(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeType: StrictStr | None = None
