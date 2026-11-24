from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsApplicationRestoreConfiguration(BaseModel):
    ApplicationRestoreType: StrictStr | None = None
    SnapshotName: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
