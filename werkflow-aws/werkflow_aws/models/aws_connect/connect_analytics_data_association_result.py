from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectAnalyticsDataAssociationResult(BaseModel):
    DataSetId: StrictStr | None = None
    TargetAccountId: StrictStr | None = None
    ResourceShareId: StrictStr | None = None
    ResourceShareArn: StrictStr | None = None
    ResourceShareStatus: StrictStr | None = None
