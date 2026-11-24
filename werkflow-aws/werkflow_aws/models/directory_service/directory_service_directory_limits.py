from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class DirectoryServiceDirectoryLimits(BaseModel):
    CloudOnlyDirectoriesLimit: StrictInt | None = None
    CloudOnlyDirectoriesCurrentCount: StrictInt | None = None
    CloudOnlyDirectoriesLimitReached: StrictBool | None = None
    CloudOnlyMicrosoftADLimit: StrictInt | None = None
    CloudOnlyMicrosoftADCurrentCount: StrictInt | None = None
    CloudOnlyMicrosoftADLimitReached: StrictBool | None = None
    ConnectedDirectoriesLimit: StrictInt | None = None
    ConnectedDirectoriesCurrentCount: StrictInt | None = None
    ConnectedDirectoriesLimitReached: StrictBool | None = None
