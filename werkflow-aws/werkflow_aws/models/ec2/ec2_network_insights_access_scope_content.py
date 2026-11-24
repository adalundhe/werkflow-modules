from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_access_scope_path import EC2AccessScopePath


class EC2NetworkInsightsAccessScopeContent(BaseModel):
    NetworkInsightsAccessScopeId: StrictStr | None = None
    MatchPaths: list[EC2AccessScopePath] | None = None
    ExcludePaths: list[EC2AccessScopePath] | None = None
