from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_logs_config import CodeBuildLogsConfig
from .code_build_project_environment import CodeBuildProjectEnvironment
from .code_build_project_file_system_location import CodeBuildProjectFileSystemLocation
from .code_build_project_source import CodeBuildProjectSource
from .code_build_project_source_version import CodeBuildProjectSourceVersion
from .code_build_sandbox_session import CodeBuildSandboxSession
from .code_build_vpc_config import CodeBuildVpcConfig


class CodeBuildSandbox(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    projectName: StrictStr | None = None
    requestTime: datetime.datetime | StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    source: CodeBuildProjectSource | None = None
    sourceVersion: StrictStr | None = None
    secondarySources: list[CodeBuildProjectSource] | None = None
    secondarySourceVersions: list[CodeBuildProjectSourceVersion] | None = None
    environment: CodeBuildProjectEnvironment | None = None
    fileSystemLocations: list[CodeBuildProjectFileSystemLocation] | None = None
    timeoutInMinutes: StrictInt | None = None
    queuedTimeoutInMinutes: StrictInt | None = None
    vpcConfig: CodeBuildVpcConfig | None = None
    logConfig: CodeBuildLogsConfig | None = None
    encryptionKey: StrictStr | None = None
    serviceRole: StrictStr | None = None
    currentSession: CodeBuildSandboxSession | None = None
