from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .code_build_compute_configuration import CodeBuildComputeConfiguration
from .code_build_docker_server import CodeBuildDockerServer
from .code_build_environment_variable import CodeBuildEnvironmentVariable
from .code_build_project_fleet import CodeBuildProjectFleet
from .code_build_registry_credential import CodeBuildRegistryCredential


class CodeBuildProjectEnvironment(BaseModel):
    type: StrictStr | None = None
    image: StrictStr | None = None
    computeType: StrictStr | None = None
    computeConfiguration: CodeBuildComputeConfiguration | None = None
    fleet: CodeBuildProjectFleet | None = None
    environmentVariables: list[CodeBuildEnvironmentVariable] | None = None
    privilegedMode: StrictBool | None = None
    certificate: StrictStr | None = None
    registryCredential: CodeBuildRegistryCredential | None = None
    imagePullCredentialsType: StrictStr | None = None
    dockerServer: CodeBuildDockerServer | None = None
    hostKernel: StrictStr | None = None
