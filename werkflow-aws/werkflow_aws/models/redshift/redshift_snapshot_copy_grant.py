from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftSnapshotCopyGrant(BaseModel):
    SnapshotCopyGrantName: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
