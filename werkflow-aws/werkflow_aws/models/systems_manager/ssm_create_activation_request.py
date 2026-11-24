from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_registration_metadata_item import SSMRegistrationMetadataItem
from .ssm_tag import SSMTag


class SSMCreateActivationRequest(BaseModel):
    IamRole: StrictStr
    Description: StrictStr | None = None
    DefaultInstanceName: StrictStr | None = None
    RegistrationLimit: StrictInt | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    Tags: list[SSMTag] | None = None
    RegistrationMetadata: list[SSMRegistrationMetadataItem] | None = None
