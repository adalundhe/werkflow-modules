from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DMSDescribeMetadataModelRequest(BaseModel):
    SelectionRules: StrictStr
    MigrationProjectIdentifier: StrictStr
    Origin: Literal['SOURCE', 'TARGET']
