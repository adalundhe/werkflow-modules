from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_accelerator_config import LambdaAcceleratorConfig
from .lambda_capacity_provider_config import LambdaCapacityProviderConfig
from .lambda_dead_letter_config import LambdaDeadLetterConfig
from .lambda_durable_config import LambdaDurableConfig
from .lambda_environment import LambdaEnvironment
from .lambda_ephemeral_storage import LambdaEphemeralStorage
from .lambda_file_system_config import LambdaFileSystemConfig
from .lambda_function_runtime_config import LambdaFunctionRuntimeConfig
from .lambda_image_config import LambdaImageConfig
from .lambda_logging_config import LambdaLoggingConfig
from .lambda_runtime import LambdaRuntime
from .lambda_snap_start import LambdaSnapStart
from .lambda_tracing_config import LambdaTracingConfig
from .lambda_vpc_config import LambdaVpcConfig


class LambdaUpdateFunctionConfigurationRequest(BaseModel):
    FunctionName: StrictStr
    Role: StrictStr | None = None
    Handler: StrictStr | None = None
    Description: StrictStr | None = None
    Timeout: StrictInt | None = None
    MemorySize: StrictInt | None = None
    VpcConfig: LambdaVpcConfig | None = None
    Environment: LambdaEnvironment | None = None
    Runtime: LambdaRuntime | None = None
    DeadLetterConfig: LambdaDeadLetterConfig | None = None
    KMSKeyArn: StrictStr | None = None
    TracingConfig: LambdaTracingConfig | None = None
    RevisionId: StrictStr | None = None
    Layers: list[StrictStr] | None = None
    FileSystemConfigs: list[LambdaFileSystemConfig] | None = None
    ImageConfig: LambdaImageConfig | None = None
    EphemeralStorage: LambdaEphemeralStorage | None = None
    SnapStart: LambdaSnapStart | None = None
    LoggingConfig: LambdaLoggingConfig | None = None
    CapacityProviderConfig: LambdaCapacityProviderConfig | None = None
    DurableConfig: LambdaDurableConfig | None = None
    RuntimeConfig: LambdaFunctionRuntimeConfig | None = None
    AcceleratorConfig: LambdaAcceleratorConfig | None = None
