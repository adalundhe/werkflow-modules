from __future__ import annotations
from pydantic import BaseModel
from .macie_job_scoping_block import MacieJobScopingBlock


class MacieScoping(BaseModel):
    excludes: MacieJobScopingBlock | None = None
    includes: MacieJobScopingBlock | None = None
