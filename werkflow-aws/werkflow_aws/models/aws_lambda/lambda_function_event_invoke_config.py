from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_destination_config_model import LambdaDestinationConfigModel


class LambdaFunctionEventInvokeConfig(BaseModel):
    LastModified: datetime.datetime | StrictStr | None = None
    FunctionArn: StrictStr | None = None
    MaximumRetryAttempts: StrictInt | None = None
    MaximumEventAgeInSeconds: StrictInt | None = None
    DestinationConfig: LambdaDestinationConfigModel | None = None
