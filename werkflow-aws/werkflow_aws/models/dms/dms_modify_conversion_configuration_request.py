from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSModifyConversionConfigurationRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    ConversionConfiguration: StrictStr
