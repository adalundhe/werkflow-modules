from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneLakeFormationConfiguration(BaseModel):
    locationRegistrationRole: StrictStr | None = None
    locationRegistrationExcludeS3Locations: list[StrictStr] | None = None
