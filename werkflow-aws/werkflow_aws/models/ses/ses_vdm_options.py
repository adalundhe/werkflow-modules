from __future__ import annotations
from pydantic import BaseModel
from .ses_dashboard_options import SESDashboardOptions
from .ses_guardian_options import SESGuardianOptions


class SESVdmOptions(BaseModel):
    DashboardOptions: SESDashboardOptions | None = None
    GuardianOptions: SESGuardianOptions | None = None
