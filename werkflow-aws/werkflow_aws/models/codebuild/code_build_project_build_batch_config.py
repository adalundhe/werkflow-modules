from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_build_batch_restrictions import CodeBuildBatchRestrictions


class CodeBuildProjectBuildBatchConfig(BaseModel):
    serviceRole: StrictStr | None = None
    combineArtifacts: StrictBool | None = None
    restrictions: CodeBuildBatchRestrictions | None = None
    timeoutInMins: StrictInt | None = None
    batchReportMode: StrictStr | None = None
