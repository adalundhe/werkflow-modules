from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_lambda_function_environment_error import SecurityHubAwsLambdaFunctionEnvironmentError


class SecurityHubAwsLambdaFunctionEnvironment(BaseModel):
    Variables: dict[StrictStr, StrictStr] | None = None
    Error: SecurityHubAwsLambdaFunctionEnvironmentError | None = None
