from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_type_id import CodePipelineActionTypeId
from .code_pipeline_artifact_detail import CodePipelineArtifactDetail


class CodePipelineActionExecutionInput(BaseModel):
    actionTypeId: CodePipelineActionTypeId | None = None
    configuration: dict[StrictStr, StrictStr] | None = None
    resolvedConfiguration: dict[StrictStr, StrictStr] | None = None
    roleArn: StrictStr | None = None
    region: StrictStr | None = None
    inputArtifacts: list[CodePipelineArtifactDetail] | None = None
    namespace: StrictStr | None = None
