from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationResourceIdentifierSummary(BaseModel):
    ResourceType: StrictStr | None = None
    LogicalResourceIds: list[StrictStr] | None = None
    ResourceIdentifiers: list[StrictStr] | None = None
