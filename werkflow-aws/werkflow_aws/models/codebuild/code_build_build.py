from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_build_auto_retry_config import CodeBuildAutoRetryConfig
from .code_build_build_artifacts import CodeBuildBuildArtifacts
from .code_build_build_phase import CodeBuildBuildPhase
from .code_build_debug_session import CodeBuildDebugSession
from .code_build_exported_environment_variable import CodeBuildExportedEnvironmentVariable
from .code_build_logs_location import CodeBuildLogsLocation
from .code_build_network_interface import CodeBuildNetworkInterface
from .code_build_project_cache import CodeBuildProjectCache
from .code_build_project_environment import CodeBuildProjectEnvironment
from .code_build_project_file_system_location import CodeBuildProjectFileSystemLocation
from .code_build_project_source import CodeBuildProjectSource
from .code_build_project_source_version import CodeBuildProjectSourceVersion
from .code_build_vpc_config import CodeBuildVpcConfig


class CodeBuildBuild(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    buildNumber: StrictInt | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    currentPhase: StrictStr | None = None
    buildStatus: StrictStr | None = None
    sourceVersion: StrictStr | None = None
    resolvedSourceVersion: StrictStr | None = None
    projectName: StrictStr | None = None
    phases: list[CodeBuildBuildPhase] | None = None
    source: CodeBuildProjectSource | None = None
    secondarySources: list[CodeBuildProjectSource] | None = None
    secondarySourceVersions: list[CodeBuildProjectSourceVersion] | None = None
    artifacts: CodeBuildBuildArtifacts | None = None
    secondaryArtifacts: list[CodeBuildBuildArtifacts] | None = None
    cache: CodeBuildProjectCache | None = None
    environment: CodeBuildProjectEnvironment | None = None
    serviceRole: StrictStr | None = None
    logs: CodeBuildLogsLocation | None = None
    timeoutInMinutes: StrictInt | None = None
    queuedTimeoutInMinutes: StrictInt | None = None
    buildComplete: StrictBool | None = None
    initiator: StrictStr | None = None
    vpcConfig: CodeBuildVpcConfig | None = None
    networkInterface: CodeBuildNetworkInterface | None = None
    encryptionKey: StrictStr | None = None
    exportedEnvironmentVariables: list[CodeBuildExportedEnvironmentVariable] | None = None
    reportArns: list[StrictStr] | None = None
    fileSystemLocations: list[CodeBuildProjectFileSystemLocation] | None = None
    debugSession: CodeBuildDebugSession | None = None
    buildBatchArn: StrictStr | None = None
    autoRetryConfig: CodeBuildAutoRetryConfig | None = None
