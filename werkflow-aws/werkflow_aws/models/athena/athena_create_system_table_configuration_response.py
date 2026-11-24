from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class AthenaCreateSystemTableConfigurationResponse(BaseModel):
    TableName: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastModifiedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
