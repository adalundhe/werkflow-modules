from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LightsailBlueprint(BaseModel):
    blueprintId: StrictStr | None = None
    name: StrictStr | None = None
    group: StrictStr | None = None
    type: StrictStr | None = None
    description: StrictStr | None = None
    isActive: StrictBool | None = None
    minPower: StrictInt | None = None
    version: StrictStr | None = None
    versionCode: StrictStr | None = None
    productUrl: StrictStr | None = None
    licenseUrl: StrictStr | None = None
    platform: StrictStr | None = None
    appCategory: StrictStr | None = None
