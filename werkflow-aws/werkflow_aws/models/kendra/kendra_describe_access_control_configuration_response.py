from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_hierarchical_principal import KendraHierarchicalPrincipal
from .kendra_principal import KendraPrincipal


class KendraDescribeAccessControlConfigurationResponse(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    AccessControlList: list[KendraPrincipal] | None = None
    HierarchicalAccessControlList: list[KendraHierarchicalPrincipal] | None = None
    ResponseMetadata: dict[str, Any] | None = None
