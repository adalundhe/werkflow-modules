from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftSnapshotErrorMessage(BaseModel):
    SnapshotIdentifier: StrictStr | None = None
    SnapshotClusterIdentifier: StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureReason: StrictStr | None = None
