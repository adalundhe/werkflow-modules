from __future__ import annotations
from pydantic import BaseModel
from .kendra_principal import KendraPrincipal


class KendraHierarchicalPrincipal(BaseModel):
    PrincipalList: list[KendraPrincipal] | None = None
