from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTDescribeCertificateProviderResponse(BaseModel):
    certificateProviderName: StrictStr | None = None
    certificateProviderArn: StrictStr | None = None
    lambdaFunctionArn: StrictStr | None = None
    accountDefaultForOperations: list[StrictStr] | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
