from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_build_logs_config import CodeBuildLogsConfig
from .code_build_project_artifacts import CodeBuildProjectArtifacts
from .code_build_project_build_batch_config import CodeBuildProjectBuildBatchConfig
from .code_build_project_cache import CodeBuildProjectCache
from .code_build_project_environment import CodeBuildProjectEnvironment
from .code_build_project_file_system_location import CodeBuildProjectFileSystemLocation
from .code_build_project_source import CodeBuildProjectSource
from .code_build_project_source_version import CodeBuildProjectSourceVersion
from .code_build_tag import CodeBuildTag
from .code_build_vpc_config import CodeBuildVpcConfig


class CodeBuildCreateProjectRequest(BaseModel):
    name: StrictStr
    source: CodeBuildProjectSource
    artifacts: CodeBuildProjectArtifacts
    environment: CodeBuildProjectEnvironment
    serviceRole: StrictStr
    description: StrictStr | None = None
    secondarySources: list[CodeBuildProjectSource] | None = None
    sourceVersion: StrictStr | None = None
    secondarySourceVersions: list[CodeBuildProjectSourceVersion] | None = None
    secondaryArtifacts: list[CodeBuildProjectArtifacts] | None = None
    cache: CodeBuildProjectCache | None = None
    timeoutInMinutes: StrictInt | None = None
    queuedTimeoutInMinutes: StrictInt | None = None
    encryptionKey: StrictStr | None = None
    tags: list[CodeBuildTag] | None = None
    vpcConfig: CodeBuildVpcConfig | None = None
    badgeEnabled: StrictBool | None = None
    logsConfig: CodeBuildLogsConfig | None = None
    fileSystemLocations: list[CodeBuildProjectFileSystemLocation] | None = None
    buildBatchConfig: CodeBuildProjectBuildBatchConfig | None = None
    concurrentBuildLimit: StrictInt | None = None
    autoRetryLimit: StrictInt | None = None
