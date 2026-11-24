from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListComputeQuotasRequest(BaseModel):
    CreatedAfter: datetime.datetime | StrictStr | None = None
    CreatedBefore: datetime.datetime | StrictStr | None = None
    NameContains: StrictStr | None = None
    Status: Literal['Creating', 'CreateFailed', 'CreateRollbackFailed', 'Created', 'Updating', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Deleting', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted'] | None = None
    ClusterArn: StrictStr | None = None
    SortBy: Literal['Name', 'CreationTime', 'Status', 'ClusterArn'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
