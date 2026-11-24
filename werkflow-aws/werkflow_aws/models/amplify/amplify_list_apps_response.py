from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amplify_app import AmplifyApp


class AmplifyListAppsResponse(BaseModel):
    apps: list[AmplifyApp] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
