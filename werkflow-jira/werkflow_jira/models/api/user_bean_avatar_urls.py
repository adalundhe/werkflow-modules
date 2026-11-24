from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictStr


class UserBeanAvatarUrls(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    size_16x16: StrictStr | None = PydanticField(default=None, alias='16x16')
    size_24x24: StrictStr | None = PydanticField(default=None, alias='24x24')
    size_32x32: StrictStr | None = PydanticField(default=None, alias='32x32')
    size_48x48: StrictStr | None = PydanticField(default=None, alias='48x48')
