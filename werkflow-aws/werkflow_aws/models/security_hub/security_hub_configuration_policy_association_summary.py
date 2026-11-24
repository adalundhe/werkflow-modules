from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubConfigurationPolicyAssociationSummary(BaseModel):
    ConfigurationPolicyId: StrictStr | None = None
    TargetId: StrictStr | None = None
    TargetType: StrictStr | None = None
    AssociationType: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    AssociationStatus: StrictStr | None = None
    AssociationStatusMessage: StrictStr | None = None
