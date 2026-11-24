from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsDeleteApplicationInputProcessingConfigurationResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
