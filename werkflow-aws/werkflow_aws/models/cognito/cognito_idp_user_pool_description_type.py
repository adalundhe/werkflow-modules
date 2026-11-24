from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cognito_idp_lambda_config_type import CognitoIDPLambdaConfigType


class CognitoIDPUserPoolDescriptionType(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    LambdaConfig: CognitoIDPLambdaConfigType | None = None
    Status: StrictStr | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    ReplicaRegions: list[StrictStr] | None = None
