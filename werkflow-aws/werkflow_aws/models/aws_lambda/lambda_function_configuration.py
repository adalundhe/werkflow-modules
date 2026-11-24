from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_accelerator_config import LambdaAcceleratorConfig
from .lambda_architecture import LambdaArchitecture
from .lambda_capacity_provider_config import LambdaCapacityProviderConfig
from .lambda_dead_letter_config import LambdaDeadLetterConfig
from .lambda_durable_config import LambdaDurableConfig
from .lambda_environment_response import LambdaEnvironmentResponse
from .lambda_ephemeral_storage import LambdaEphemeralStorage
from .lambda_file_system_config import LambdaFileSystemConfig
from .lambda_function_runtime_config import LambdaFunctionRuntimeConfig
from .lambda_image_config_response import LambdaImageConfigResponse
from .lambda_last_update_status import LambdaLastUpdateStatus
from .lambda_last_update_status_reason_code import LambdaLastUpdateStatusReasonCode
from .lambda_layer import LambdaLayer
from .lambda_logging_config import LambdaLoggingConfig
from .lambda_package_type import LambdaPackageType
from .lambda_runtime import LambdaRuntime
from .lambda_runtime_version_config import LambdaRuntimeVersionConfig
from .lambda_snap_start_response import LambdaSnapStartResponse
from .lambda_state import LambdaState
from .lambda_state_reason_code import LambdaStateReasonCode
from .lambda_tenancy_config import LambdaTenancyConfig
from .lambda_tracing_config_response import LambdaTracingConfigResponse
from .lambda_vpc_config_response import LambdaVpcConfigResponse


class LambdaFunctionConfiguration(BaseModel):
    FunctionName: StrictStr | None = None
    FunctionArn: StrictStr | None = None
    Runtime: LambdaRuntime | None = None
    Role: StrictStr | None = None
    Handler: StrictStr | None = None
    CodeSize: StrictInt | None = None
    Description: StrictStr | None = None
    Timeout: StrictInt | None = None
    MemorySize: StrictInt | None = None
    LastModified: StrictStr | None = None
    CodeSha256: StrictStr | None = None
    Version: StrictStr | None = None
    VpcConfig: LambdaVpcConfigResponse | None = None
    DeadLetterConfig: LambdaDeadLetterConfig | None = None
    Environment: LambdaEnvironmentResponse | None = None
    KMSKeyArn: StrictStr | None = None
    TracingConfig: LambdaTracingConfigResponse | None = None
    MasterArn: StrictStr | None = None
    RevisionId: StrictStr | None = None
    Layers: list[LambdaLayer] | None = None
    State: LambdaState | None = None
    StateReason: StrictStr | None = None
    StateReasonCode: LambdaStateReasonCode | None = None
    LastUpdateStatus: LambdaLastUpdateStatus | None = None
    LastUpdateStatusReason: StrictStr | None = None
    LastUpdateStatusReasonCode: LambdaLastUpdateStatusReasonCode | None = None
    FileSystemConfigs: list[LambdaFileSystemConfig] | None = None
    SigningProfileVersionArn: StrictStr | None = None
    SigningJobArn: StrictStr | None = None
    PackageType: LambdaPackageType | None = None
    ImageConfigResponse: LambdaImageConfigResponse | None = None
    Architectures: list[LambdaArchitecture] | None = None
    EphemeralStorage: LambdaEphemeralStorage | None = None
    SnapStart: LambdaSnapStartResponse | None = None
    RuntimeVersionConfig: LambdaRuntimeVersionConfig | None = None
    LoggingConfig: LambdaLoggingConfig | None = None
    TenancyConfig: LambdaTenancyConfig | None = None
    CapacityProviderConfig: LambdaCapacityProviderConfig | None = None
    ConfigSha256: StrictStr | None = None
    DurableConfig: LambdaDurableConfig | None = None
    RuntimeConfig: LambdaFunctionRuntimeConfig | None = None
    AcceleratorConfig: LambdaAcceleratorConfig | None = None
