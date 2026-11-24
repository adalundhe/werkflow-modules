from __future__ import annotations
from pydantic import BaseModel
from .mskebs_storage_info_model import MSKEBSStorageInfoModel


class MSKStorageInfo(BaseModel):
    EbsStorageInfo: MSKEBSStorageInfoModel | None = None
