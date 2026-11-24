from __future__ import annotations
from pydantic import BaseModel
from .ecr_signing_rule import ECRSigningRule


class ECRSigningConfiguration(BaseModel):
    rules: list[ECRSigningRule] | None = None
