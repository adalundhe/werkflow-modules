from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTServerCertificateConfig(BaseModel):
    enableOCSPCheck: StrictBool | None = None
    ocspLambdaArn: StrictStr | None = None
    ocspAuthorizedResponderArn: StrictStr | None = None
