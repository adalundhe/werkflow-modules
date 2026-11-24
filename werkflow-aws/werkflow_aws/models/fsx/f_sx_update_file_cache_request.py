from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_update_file_cache_lustre_configuration import FSxUpdateFileCacheLustreConfiguration


class FSxUpdateFileCacheRequest(BaseModel):
    FileCacheId: StrictStr
    ClientRequestToken: StrictStr | None = None
    LustreConfiguration: FSxUpdateFileCacheLustreConfiguration | None = None
