from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class IoTUpdateCertificateProviderRequest(BaseModel):
    certificateProviderName: StrictStr
    lambdaFunctionArn: StrictStr | None = None
    accountDefaultForOperations: list[Literal['CreateCertificateFromCsr']] | None = None
