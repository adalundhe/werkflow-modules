from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPFirehoseConfigurationType(BaseModel):
    StreamArn: StrictStr | None = None
