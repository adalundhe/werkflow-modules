from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightDeleteFolderMembershipRequest(BaseModel):
    AwsAccountId: StrictStr
    FolderId: StrictStr
    MemberId: StrictStr
    MemberType: Literal['DASHBOARD', 'ANALYSIS', 'DATASET', 'DATASOURCE', 'TOPIC']
