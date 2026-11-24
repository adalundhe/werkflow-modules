from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt
from .global_scope_bean import GlobalScopeBean
from .project_scope_bean import ProjectScopeBean


class IssueFieldOptionScopeBean(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    global_: GlobalScopeBean | None = PydanticField(default=None, alias='global')
    projects: list[StrictInt] | None = None
    projects2: list[ProjectScopeBean] | None = None
