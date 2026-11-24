from __future__ import annotations
from typing import BinaryIO
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class CognitoIDPSetUICustomizationRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    UserPoolId: StrictStr
    ClientId: StrictStr | None = None
    CSS: StrictStr | None = None
    ImageFile: StrictBytes | BinaryIO | StrictStr | None = None
