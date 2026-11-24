from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateIdentityPropagationConfigRequest(BaseModel):
    AwsAccountId: StrictStr
    Service: Literal['REDSHIFT', 'QBUSINESS', 'ATHENA', 'GLUE_DATA_CATALOG']
    AuthorizedTargets: list[StrictStr] | None = None
