from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectAssociateAnalyticsDataSetResponse(BaseModel):
    DataSetId: StrictStr | None = None
    TargetAccountId: StrictStr | None = None
    ResourceShareId: StrictStr | None = None
    ResourceShareArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
