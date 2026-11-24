from __future__ import annotations
from pydantic import BaseModel
from .lex_buildtime_settings import LexBuildtimeSettings
from .lex_runtime_settings import LexRuntimeSettings


class LexGenerativeAISettings(BaseModel):
    runtimeSettings: LexRuntimeSettings | None = None
    buildtimeSettings: LexBuildtimeSettings | None = None
