from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsDynamoDbTableKeySchema(BaseModel):
    AttributeName: StrictStr | None = None
    KeyType: StrictStr | None = None
