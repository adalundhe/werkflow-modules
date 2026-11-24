from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2EnableImageBlockPublicAccessRequest(BaseModel):
    ImageBlockPublicAccessState: Literal['block-new-sharing']
    DryRun: StrictBool | None = None
