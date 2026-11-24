from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lambda_accelerator_config import LambdaAcceleratorConfig
from .lambda_architecture import LambdaArchitecture
from .lambda_capacity_provider_config import LambdaCapacityProviderConfig
from .lambda_dead_letter_config import LambdaDeadLetterConfig
from .lambda_durable_config import LambdaDurableConfig
from .lambda_environment import LambdaEnvironment
from .lambda_ephemeral_storage import LambdaEphemeralStorage
from .lambda_file_system_config import LambdaFileSystemConfig
from .lambda_function_code import LambdaFunctionCode
from .lambda_function_runtime_config import LambdaFunctionRuntimeConfig
from .lambda_function_version_latest_published import LambdaFunctionVersionLatestPublished
from .lambda_image_config import LambdaImageConfig
from .lambda_logging_config import LambdaLoggingConfig
from .lambda_package_type import LambdaPackageType
from .lambda_runtime import LambdaRuntime
from .lambda_snap_start import LambdaSnapStart
from .lambda_tenancy_config import LambdaTenancyConfig
from .lambda_tracing_config import LambdaTracingConfig
from .lambda_vpc_config import LambdaVpcConfig


class LambdaCreateFunctionRequest(BaseModel):
    FunctionName: StrictStr
    Role: StrictStr
    Code: LambdaFunctionCode
    Runtime: LambdaRuntime | None = None
    Handler: StrictStr | None = None
    Description: StrictStr | None = None
    Timeout: StrictInt | None = None
    MemorySize: StrictInt | None = None
    Publish: StrictBool | None = None
    PublishTo: LambdaFunctionVersionLatestPublished | None = None
    VpcConfig: LambdaVpcConfig | None = None
    PackageType: LambdaPackageType | None = None
    DeadLetterConfig: LambdaDeadLetterConfig | None = None
    Environment: LambdaEnvironment | None = None
    KMSKeyArn: StrictStr | None = None
    TracingConfig: LambdaTracingConfig | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Layers: list[StrictStr] | None = None
    FileSystemConfigs: list[LambdaFileSystemConfig] | None = None
    CodeSigningConfigArn: StrictStr | None = None
    ImageConfig: LambdaImageConfig | None = None
    Architectures: list[LambdaArchitecture] | None = None
    EphemeralStorage: LambdaEphemeralStorage | None = None
    SnapStart: LambdaSnapStart | None = None
    LoggingConfig: LambdaLoggingConfig | None = None
    TenancyConfig: LambdaTenancyConfig | None = None
    CapacityProviderConfig: LambdaCapacityProviderConfig | None = None
    DurableConfig: LambdaDurableConfig | None = None
    RuntimeConfig: LambdaFunctionRuntimeConfig | None = None
    AcceleratorConfig: LambdaAcceleratorConfig | None = None
