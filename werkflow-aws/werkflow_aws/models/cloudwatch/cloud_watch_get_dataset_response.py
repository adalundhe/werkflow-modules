from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudWatchGetDatasetResponse(BaseModel):
    DatasetId: StrictStr | None = None
    Arn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
