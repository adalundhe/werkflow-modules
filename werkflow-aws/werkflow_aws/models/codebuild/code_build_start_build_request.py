from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .code_build_build_status_config import CodeBuildBuildStatusConfig
from .code_build_environment_variable import CodeBuildEnvironmentVariable
from .code_build_git_submodules_config import CodeBuildGitSubmodulesConfig
from .code_build_logs_config import CodeBuildLogsConfig
from .code_build_project_artifacts import CodeBuildProjectArtifacts
from .code_build_project_cache import CodeBuildProjectCache
from .code_build_project_fleet import CodeBuildProjectFleet
from .code_build_project_source import CodeBuildProjectSource
from .code_build_project_source_version import CodeBuildProjectSourceVersion
from .code_build_registry_credential import CodeBuildRegistryCredential
from .code_build_source_auth import CodeBuildSourceAuth


class CodeBuildStartBuildRequest(BaseModel):
    projectName: StrictStr
    secondarySourcesOverride: list[CodeBuildProjectSource] | None = None
    secondarySourcesVersionOverride: list[CodeBuildProjectSourceVersion] | None = None
    sourceVersion: StrictStr | None = None
    artifactsOverride: CodeBuildProjectArtifacts | None = None
    secondaryArtifactsOverride: list[CodeBuildProjectArtifacts] | None = None
    environmentVariablesOverride: list[CodeBuildEnvironmentVariable] | None = None
    sourceTypeOverride: Literal['CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITLAB', 'GITLAB_SELF_MANAGED', 'S3', 'BITBUCKET', 'GITHUB_ENTERPRISE', 'NO_SOURCE'] | None = None
    sourceLocationOverride: StrictStr | None = None
    sourceAuthOverride: CodeBuildSourceAuth | None = None
    gitCloneDepthOverride: StrictInt | None = None
    gitSubmodulesConfigOverride: CodeBuildGitSubmodulesConfig | None = None
    buildspecOverride: StrictStr | None = None
    insecureSslOverride: StrictBool | None = None
    reportBuildStatusOverride: StrictBool | None = None
    buildStatusConfigOverride: CodeBuildBuildStatusConfig | None = None
    environmentTypeOverride: Literal['WINDOWS_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'ARM_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER', 'WINDOWS_SERVER_2022_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_EC2', 'ARM_EC2', 'WINDOWS_EC2', 'MAC_ARM'] | None = None
    imageOverride: StrictStr | None = None
    computeTypeOverride: Literal['BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_XLARGE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB', 'BUILD_LAMBDA_10GB', 'ATTRIBUTE_BASED_COMPUTE', 'CUSTOM_INSTANCE_TYPE'] | None = None
    certificateOverride: StrictStr | None = None
    cacheOverride: CodeBuildProjectCache | None = None
    serviceRoleOverride: StrictStr | None = None
    privilegedModeOverride: StrictBool | None = None
    timeoutInMinutesOverride: StrictInt | None = None
    queuedTimeoutInMinutesOverride: StrictInt | None = None
    encryptionKeyOverride: StrictStr | None = None
    idempotencyToken: StrictStr | None = None
    logsConfigOverride: CodeBuildLogsConfig | None = None
    registryCredentialOverride: CodeBuildRegistryCredential | None = None
    imagePullCredentialsTypeOverride: Literal['CODEBUILD', 'SERVICE_ROLE'] | None = None
    debugSessionEnabled: StrictBool | None = None
    fleetOverride: CodeBuildProjectFleet | None = None
    autoRetryLimitOverride: StrictInt | None = None
    hostKernelOverride: Literal['LINUX_KERNEL_4', 'LINUX_KERNEL_6', 'LINUX_KERNEL_LATEST'] | None = None
