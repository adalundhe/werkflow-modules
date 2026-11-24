from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockTrustedAccessProgramProviderHandoff(BaseModel):
    enrollmentUrl: StrictStr | None = None
    applicationToken: StrictStr | None = None
    applicationTokenExpiresAt: datetime.datetime | StrictStr | None = None
