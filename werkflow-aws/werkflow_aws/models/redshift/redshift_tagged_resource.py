from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftTaggedResource(BaseModel):
    Tag: RedshiftTag | None = None
    ResourceName: StrictStr | None = None
    ResourceType: StrictStr | None = None
