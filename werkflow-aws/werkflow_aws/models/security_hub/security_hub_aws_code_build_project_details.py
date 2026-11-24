from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_code_build_project_artifacts_details import SecurityHubAwsCodeBuildProjectArtifactsDetails
from .security_hub_aws_code_build_project_environment import SecurityHubAwsCodeBuildProjectEnvironment
from .security_hub_aws_code_build_project_logs_config_details import SecurityHubAwsCodeBuildProjectLogsConfigDetails
from .security_hub_aws_code_build_project_source import SecurityHubAwsCodeBuildProjectSource
from .security_hub_aws_code_build_project_vpc_config import SecurityHubAwsCodeBuildProjectVpcConfig


class SecurityHubAwsCodeBuildProjectDetails(BaseModel):
    EncryptionKey: StrictStr | None = None
    Artifacts: list[SecurityHubAwsCodeBuildProjectArtifactsDetails] | None = None
    Environment: SecurityHubAwsCodeBuildProjectEnvironment | None = None
    Name: StrictStr | None = None
    Source: SecurityHubAwsCodeBuildProjectSource | None = None
    ServiceRole: StrictStr | None = None
    LogsConfig: SecurityHubAwsCodeBuildProjectLogsConfigDetails | None = None
    VpcConfig: SecurityHubAwsCodeBuildProjectVpcConfig | None = None
    SecondaryArtifacts: list[SecurityHubAwsCodeBuildProjectArtifactsDetails] | None = None
