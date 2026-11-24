from __future__ import annotations
from pydantic import BaseModel
from .ssm_patch_filter import SSMPatchFilter


class SSMPatchFilterGroup(BaseModel):
    PatchFilters: list[SSMPatchFilter] | None = None
