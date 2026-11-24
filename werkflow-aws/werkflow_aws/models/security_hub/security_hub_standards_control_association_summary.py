from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubStandardsControlAssociationSummary(BaseModel):
    StandardsArn: StrictStr | None = None
    SecurityControlId: StrictStr | None = None
    SecurityControlArn: StrictStr | None = None
    AssociationStatus: StrictStr | None = None
    RelatedRequirements: list[StrictStr] | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    UpdatedReason: StrictStr | None = None
    StandardsControlTitle: StrictStr | None = None
    StandardsControlDescription: StrictStr | None = None
