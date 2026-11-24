from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationTypeConfigurationDetails(BaseModel):
    Arn: StrictStr | None = None
    Alias: StrictStr | None = None
    Configuration: StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    TypeArn: StrictStr | None = None
    TypeName: StrictStr | None = None
    IsDefaultConfiguration: StrictBool | None = None
