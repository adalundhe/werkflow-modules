from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDescribeApplicableIndividualAssessmentsRequest(BaseModel):
    ReplicationTaskArn: StrictStr | None = None
    ReplicationInstanceArn: StrictStr | None = None
    ReplicationConfigArn: StrictStr | None = None
    SourceEngineName: StrictStr | None = None
    TargetEngineName: StrictStr | None = None
    MigrationType: Literal['full-load', 'cdc', 'full-load-and-cdc'] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
