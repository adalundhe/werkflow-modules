from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_code_build_project_environment_environment_variables_details import SecurityHubAwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails
from .security_hub_aws_code_build_project_environment_registry_credential import SecurityHubAwsCodeBuildProjectEnvironmentRegistryCredential


class SecurityHubAwsCodeBuildProjectEnvironment(BaseModel):
    Certificate: StrictStr | None = None
    EnvironmentVariables: list[SecurityHubAwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails] | None = None
    PrivilegedMode: StrictBool | None = None
    ImagePullCredentialsType: StrictStr | None = None
    RegistryCredential: SecurityHubAwsCodeBuildProjectEnvironmentRegistryCredential | None = None
    Type: StrictStr | None = None
