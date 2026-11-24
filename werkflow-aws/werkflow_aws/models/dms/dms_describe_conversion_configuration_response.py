from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DMSDescribeConversionConfigurationResponse(BaseModel):
    MigrationProjectIdentifier: StrictStr | None = None
    ConversionConfiguration: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
