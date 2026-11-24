from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_action_type_id import CodePipelineActionTypeId
from .code_pipeline_environment_variable import CodePipelineEnvironmentVariable
from .code_pipeline_input_artifact import CodePipelineInputArtifact
from .code_pipeline_output_artifact import CodePipelineOutputArtifact


class CodePipelineActionDeclaration(BaseModel):
    name: StrictStr | None = None
    actionTypeId: CodePipelineActionTypeId | None = None
    runOrder: StrictInt | None = None
    configuration: dict[StrictStr, StrictStr] | None = None
    commands: list[StrictStr] | None = None
    outputArtifacts: list[CodePipelineOutputArtifact] | None = None
    inputArtifacts: list[CodePipelineInputArtifact] | None = None
    outputVariables: list[StrictStr] | None = None
    roleArn: StrictStr | None = None
    region: StrictStr | None = None
    namespace: StrictStr | None = None
    timeoutInMinutes: StrictInt | None = None
    environmentVariables: list[CodePipelineEnvironmentVariable] | None = None
