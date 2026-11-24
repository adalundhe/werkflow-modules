from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2EnableSnapshotBlockPublicAccessRequest(BaseModel):
    State: Literal['block-all-sharing', 'block-new-sharing', 'unblocked']
    DryRun: StrictBool | None = None
