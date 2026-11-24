from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDescribeStudioLifecycleConfigResponse(BaseModel):
    StudioLifecycleConfigArn: StrictStr | None = None
    StudioLifecycleConfigName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    StudioLifecycleConfigContent: StrictStr | None = None
    StudioLifecycleConfigAppType: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
