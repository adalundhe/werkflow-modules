from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightExternalIdpConfidentialClientSecret(BaseModel):
    ClientSecretId: StrictStr | None = None
    RegionalSecretManagerArns: dict[StrictStr, StrictStr] | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
