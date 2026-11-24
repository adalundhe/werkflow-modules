from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_tag import IoTTag


class IoTCreateCertificateProviderRequest(BaseModel):
    certificateProviderName: StrictStr
    lambdaFunctionArn: StrictStr
    accountDefaultForOperations: list[Literal['CreateCertificateFromCsr']]
    clientToken: StrictStr | None = None
    tags: list[IoTTag] | None = None
