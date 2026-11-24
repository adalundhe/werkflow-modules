from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_dashboard_attributes import SESDashboardAttributes
from .ses_guardian_attributes import SESGuardianAttributes


class SESVdmAttributes(BaseModel):
    VdmEnabled: StrictStr | None = None
    DashboardAttributes: SESDashboardAttributes | None = None
    GuardianAttributes: SESGuardianAttributes | None = None
