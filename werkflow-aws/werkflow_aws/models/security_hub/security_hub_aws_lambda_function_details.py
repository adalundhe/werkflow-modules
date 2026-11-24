from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_lambda_function_code import SecurityHubAwsLambdaFunctionCode
from .security_hub_aws_lambda_function_dead_letter_config import SecurityHubAwsLambdaFunctionDeadLetterConfig
from .security_hub_aws_lambda_function_environment import SecurityHubAwsLambdaFunctionEnvironment
from .security_hub_aws_lambda_function_layer import SecurityHubAwsLambdaFunctionLayer
from .security_hub_aws_lambda_function_tracing_config import SecurityHubAwsLambdaFunctionTracingConfig
from .security_hub_aws_lambda_function_vpc_config import SecurityHubAwsLambdaFunctionVpcConfig


class SecurityHubAwsLambdaFunctionDetails(BaseModel):
    Code: SecurityHubAwsLambdaFunctionCode | None = None
    CodeSha256: StrictStr | None = None
    DeadLetterConfig: SecurityHubAwsLambdaFunctionDeadLetterConfig | None = None
    Environment: SecurityHubAwsLambdaFunctionEnvironment | None = None
    FunctionName: StrictStr | None = None
    Handler: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    LastModified: StrictStr | None = None
    Layers: list[SecurityHubAwsLambdaFunctionLayer] | None = None
    MasterArn: StrictStr | None = None
    MemorySize: StrictInt | None = None
    RevisionId: StrictStr | None = None
    Role: StrictStr | None = None
    Runtime: StrictStr | None = None
    Timeout: StrictInt | None = None
    TracingConfig: SecurityHubAwsLambdaFunctionTracingConfig | None = None
    VpcConfig: SecurityHubAwsLambdaFunctionVpcConfig | None = None
    Version: StrictStr | None = None
    Architectures: list[StrictStr] | None = None
    PackageType: StrictStr | None = None
