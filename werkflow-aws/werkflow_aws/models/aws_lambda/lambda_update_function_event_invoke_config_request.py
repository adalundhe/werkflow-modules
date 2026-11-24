from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_destination_config_model import LambdaDestinationConfigModel


class LambdaUpdateFunctionEventInvokeConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr | None = None
    MaximumRetryAttempts: StrictInt | None = None
    MaximumEventAgeInSeconds: StrictInt | None = None
    DestinationConfig: LambdaDestinationConfigModel | None = None
