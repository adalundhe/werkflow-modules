from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAuthorizeSnapshotAccessRequest(BaseModel):
    AccountWithRestoreAccess: StrictStr
    SnapshotIdentifier: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    SnapshotClusterIdentifier: StrictStr | None = None
