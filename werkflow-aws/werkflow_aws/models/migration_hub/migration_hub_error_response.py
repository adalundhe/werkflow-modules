from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MigrationHubErrorResponse(BaseModel):
    AccountId: StrictStr | None = None
    AdditionalDetails: dict[StrictStr, StrictStr] | None = None
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    ResourceIdentifier: StrictStr | None = None
    ResourceType: StrictStr | None = None
