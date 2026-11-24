from __future__ import annotations
from pydantic import BaseModel
from typing import Literal


class AWSS3GetBucketVersioningResponse(BaseModel):
    Status: Literal['Enabled', 'Suspended'] | None = None
    MFADelete: Literal['Enabled', 'Disabled'] | None = None
