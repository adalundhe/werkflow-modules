from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAATeamConfig(BaseModel):
    SourceBucketArn: StrictStr | None = None
    DagS3Path: StrictStr | None = None
