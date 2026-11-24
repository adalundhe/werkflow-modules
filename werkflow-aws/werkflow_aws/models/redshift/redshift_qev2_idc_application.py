from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftQev2IdcApplication(BaseModel):
    IdcInstanceArn: StrictStr | None = None
    Qev2IdcApplicationName: StrictStr | None = None
    Qev2IdcApplicationArn: StrictStr | None = None
    IdcManagedApplicationArn: StrictStr | None = None
    IdcOnboardStatus: StrictStr | None = None
    IdcDisplayName: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
