from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsDeleteApplicationVpcConfigurationResponse(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    OperationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
