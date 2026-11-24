from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDescribeConversionConfigurationRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
