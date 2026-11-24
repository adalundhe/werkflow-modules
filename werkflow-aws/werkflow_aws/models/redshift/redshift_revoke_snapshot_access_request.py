from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftRevokeSnapshotAccessRequest(BaseModel):
    AccountWithRestoreAccess: StrictStr
    SnapshotIdentifier: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    SnapshotClusterIdentifier: StrictStr | None = None
