from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_logs_config import CodeBuildLogsConfig
from .code_build_project_artifacts import CodeBuildProjectArtifacts
from .code_build_project_badge import CodeBuildProjectBadge
from .code_build_project_build_batch_config import CodeBuildProjectBuildBatchConfig
from .code_build_project_cache import CodeBuildProjectCache
from .code_build_project_environment import CodeBuildProjectEnvironment
from .code_build_project_file_system_location import CodeBuildProjectFileSystemLocation
from .code_build_project_source import CodeBuildProjectSource
from .code_build_project_source_version import CodeBuildProjectSourceVersion
from .code_build_tag import CodeBuildTag
from .code_build_vpc_config import CodeBuildVpcConfig
from .code_build_webhook import CodeBuildWebhook


class CodeBuildProject(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    source: CodeBuildProjectSource | None = None
    secondarySources: list[CodeBuildProjectSource] | None = None
    sourceVersion: StrictStr | None = None
    secondarySourceVersions: list[CodeBuildProjectSourceVersion] | None = None
    artifacts: CodeBuildProjectArtifacts | None = None
    secondaryArtifacts: list[CodeBuildProjectArtifacts] | None = None
    cache: CodeBuildProjectCache | None = None
    environment: CodeBuildProjectEnvironment | None = None
    serviceRole: StrictStr | None = None
    timeoutInMinutes: StrictInt | None = None
    queuedTimeoutInMinutes: StrictInt | None = None
    encryptionKey: StrictStr | None = None
    tags: list[CodeBuildTag] | None = None
    created: datetime.datetime | StrictStr | None = None
    lastModified: datetime.datetime | StrictStr | None = None
    webhook: CodeBuildWebhook | None = None
    vpcConfig: CodeBuildVpcConfig | None = None
    badge: CodeBuildProjectBadge | None = None
    logsConfig: CodeBuildLogsConfig | None = None
    fileSystemLocations: list[CodeBuildProjectFileSystemLocation] | None = None
    buildBatchConfig: CodeBuildProjectBuildBatchConfig | None = None
    concurrentBuildLimit: StrictInt | None = None
    projectVisibility: StrictStr | None = None
    publicProjectAlias: StrictStr | None = None
    resourceAccessRole: StrictStr | None = None
    autoRetryLimit: StrictInt | None = None
