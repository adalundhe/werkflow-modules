from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeHybridADUpdateRequest(BaseModel):
    DirectoryId: StrictStr
    UpdateType: Literal['SelfManagedInstances', 'HybridAdministratorAccount'] | None = None
    NextToken: StrictStr | None = None
