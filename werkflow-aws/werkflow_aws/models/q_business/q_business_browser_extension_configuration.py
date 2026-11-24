from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessBrowserExtensionConfiguration(BaseModel):
    enabledBrowserExtensions: list[StrictStr] | None = None
