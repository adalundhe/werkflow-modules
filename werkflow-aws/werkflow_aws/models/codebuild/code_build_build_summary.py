from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_build_resolved_artifact import CodeBuildResolvedArtifact


class CodeBuildBuildSummary(BaseModel):
    arn: StrictStr | None = None
    requestedOn: datetime.datetime | StrictStr | None = None
    buildStatus: StrictStr | None = None
    primaryArtifact: CodeBuildResolvedArtifact | None = None
    secondaryArtifacts: list[CodeBuildResolvedArtifact] | None = None
