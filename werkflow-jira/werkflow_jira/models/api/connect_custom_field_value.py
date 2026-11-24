from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictFloat, StrictInt, StrictStr


class ConnectCustomFieldValue(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    type_: StrictStr | None = PydanticField(default=None, alias='_type')
    fieldID: StrictInt | None = None
    issueID: StrictInt | None = None
    number: StrictFloat | StrictInt | None = None
    optionID: StrictStr | None = None
    richText: StrictStr | None = None
    string: StrictStr | None = None
    text: StrictStr | None = None
