from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_hierarchical_principal import KendraHierarchicalPrincipal
from .kendra_principal import KendraPrincipal


class KendraUpdateAccessControlConfigurationRequest(BaseModel):
    IndexId: StrictStr
    Id: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    AccessControlList: list[KendraPrincipal] | None = None
    HierarchicalAccessControlList: list[KendraHierarchicalPrincipal] | None = None
