from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSGetParametersForImportResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr | None = None
    ImportToken: StrictBytes | Any | None = None
    PublicKey: StrictBytes | Any | None = None
    ParametersValidTo: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
