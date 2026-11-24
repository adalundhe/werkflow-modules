from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerListModelPackagesRequest(BaseModel):
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
    MaxResults: StrictInt | None = None
    NameContains: StrictStr | None = None
    ModelApprovalStatus: Literal['Approved', 'Rejected', 'PendingManualApproval'] | None = None
    ModelPackageGroupName: StrictStr | None = None
    ModelPackageType: Literal['Versioned', 'Unversioned', 'Both'] | None = None
    NextToken: StrictStr | None = None
    SortBy: Literal['Name', 'CreationTime'] | None = None
    SortOrder: Literal['Ascending', 'Descending'] | None = None
