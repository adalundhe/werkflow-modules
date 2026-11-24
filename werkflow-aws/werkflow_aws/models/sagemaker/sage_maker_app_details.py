from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_resource_spec import SageMakerResourceSpec


class SageMakerAppDetails(BaseModel):
    DomainId: StrictStr | None = None
    UserProfileName: StrictStr | None = None
    SpaceName: StrictStr | None = None
    AppType: StrictStr | None = None
    AppName: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResourceSpec: SageMakerResourceSpec | None = None
