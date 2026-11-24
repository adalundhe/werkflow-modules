from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class ECSDeleteDaemonResponse(BaseModel):
    daemonArn: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    deploymentArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
