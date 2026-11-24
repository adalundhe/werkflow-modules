from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DMSDescribeMetadataModelChildrenRequest(BaseModel):
    SelectionRules: StrictStr
    MigrationProjectIdentifier: StrictStr
    Origin: Literal['SOURCE', 'TARGET']
    Marker: StrictStr | None = None
    MaxRecords: StrictInt | None = None
