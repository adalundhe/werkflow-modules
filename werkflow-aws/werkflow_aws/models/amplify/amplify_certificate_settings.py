from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AmplifyCertificateSettings(BaseModel):
    type: Literal['AMPLIFY_MANAGED', 'CUSTOM']
    customCertificateArn: StrictStr | None = None
