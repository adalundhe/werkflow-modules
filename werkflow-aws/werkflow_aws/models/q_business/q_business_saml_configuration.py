from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessSamlConfiguration(BaseModel):
    metadataXML: StrictStr | None = None
    roleArn: StrictStr | None = None
    userIdAttribute: StrictStr | None = None
    userGroupAttribute: StrictStr | None = None
