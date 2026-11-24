from __future__ import annotations
from pydantic import BaseModel
from .ssm_patch_rule import SSMPatchRule


class SSMPatchRuleGroup(BaseModel):
    PatchRules: list[SSMPatchRule] | None = None
