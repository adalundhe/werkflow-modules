from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_artifact_package_group_summary import CodeArtifactPackageGroupSummary


class CodeArtifactListSubPackageGroupsResponse(BaseModel):
    packageGroups: list[CodeArtifactPackageGroupSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
