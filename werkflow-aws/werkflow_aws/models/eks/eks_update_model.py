from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_cancellation_model import EKSCancellationModel
from .eks_error_detail_model import EKSErrorDetailModel
from .eks_update_param_model import EKSUpdateParamModel


class EKSUpdateModel(BaseModel):
    id: StrictStr | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
    params: list[EKSUpdateParamModel] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    errors: list[EKSErrorDetailModel] | None = None
    cancellation: EKSCancellationModel | None = None
