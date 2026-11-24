from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_app import AmplifyApp


class AmplifyCreateAppResponse(BaseModel):
    app: AmplifyApp | None = None
    ResponseMetadata: dict[str, Any] | None = None
