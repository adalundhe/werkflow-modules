from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_build_build_artifacts import CodeBuildBuildArtifacts
from .code_build_build_batch_phase import CodeBuildBuildBatchPhase
from .code_build_build_group import CodeBuildBuildGroup
from .code_build_logs_config import CodeBuildLogsConfig
from .code_build_project_build_batch_config import CodeBuildProjectBuildBatchConfig
from .code_build_project_cache import CodeBuildProjectCache
from .code_build_project_environment import CodeBuildProjectEnvironment
from .code_build_project_file_system_location import CodeBuildProjectFileSystemLocation
from .code_build_project_source import CodeBuildProjectSource
from .code_build_project_source_version import CodeBuildProjectSourceVersion
from .code_build_vpc_config import CodeBuildVpcConfig


class CodeBuildBuildBatch(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    currentPhase: StrictStr | None = None
    buildBatchStatus: StrictStr | None = None
    sourceVersion: StrictStr | None = None
    resolvedSourceVersion: StrictStr | None = None
    projectName: StrictStr | None = None
    phases: list[CodeBuildBuildBatchPhase] | None = None
    source: CodeBuildProjectSource | None = None
    secondarySources: list[CodeBuildProjectSource] | None = None
    secondarySourceVersions: list[CodeBuildProjectSourceVersion] | None = None
    artifacts: CodeBuildBuildArtifacts | None = None
    secondaryArtifacts: list[CodeBuildBuildArtifacts] | None = None
    cache: CodeBuildProjectCache | None = None
    environment: CodeBuildProjectEnvironment | None = None
    serviceRole: StrictStr | None = None
    logConfig: CodeBuildLogsConfig | None = None
    buildTimeoutInMinutes: StrictInt | None = None
    queuedTimeoutInMinutes: StrictInt | None = None
    complete: StrictBool | None = None
    initiator: StrictStr | None = None
    vpcConfig: CodeBuildVpcConfig | None = None
    encryptionKey: StrictStr | None = None
    buildBatchNumber: StrictInt | None = None
    fileSystemLocations: list[CodeBuildProjectFileSystemLocation] | None = None
    buildBatchConfig: CodeBuildProjectBuildBatchConfig | None = None
    buildGroups: list[CodeBuildBuildGroup] | None = None
    debugSessionEnabled: StrictBool | None = None
    reportArns: list[StrictStr] | None = None
