from __future__ import annotations
from pydantic import BaseModel
from .macie_simple_scope_term import MacieSimpleScopeTerm
from .macie_tag_scope_term import MacieTagScopeTerm


class MacieJobScopeTerm(BaseModel):
    simpleScopeTerm: MacieSimpleScopeTerm | None = None
    tagScopeTerm: MacieTagScopeTerm | None = None
