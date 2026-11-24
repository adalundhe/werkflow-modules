from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KMSRotationsListEntry(BaseModel):
    KeyId: StrictStr | None = None
    KeyMaterialId: StrictStr | None = None
    KeyMaterialDescription: StrictStr | None = None
    ImportState: StrictStr | None = None
    KeyMaterialState: StrictStr | None = None
    ExpirationModel: StrictStr | None = None
    ValidTo: datetime.datetime | StrictStr | None = None
    RotationDate: datetime.datetime | StrictStr | None = None
    RotationType: StrictStr | None = None
