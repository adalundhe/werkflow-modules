from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .awss3_object_identifier import AWSS3ObjectIdentifier


class AWSS3Delete(BaseModel):
    Objects: list[AWSS3ObjectIdentifier]
    Quiet: StrictBool | None = None
