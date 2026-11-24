from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubStandardsControl(BaseModel):
    StandardsControlArn: StrictStr | None = None
    ControlStatus: StrictStr | None = None
    DisabledReason: StrictStr | None = None
    ControlStatusUpdatedAt: datetime.datetime | StrictStr | None = None
    ControlId: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    RemediationUrl: StrictStr | None = None
    SeverityRating: StrictStr | None = None
    RelatedRequirements: list[StrictStr] | None = None
