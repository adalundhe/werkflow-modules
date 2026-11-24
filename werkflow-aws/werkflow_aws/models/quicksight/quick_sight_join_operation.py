from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_join_operand_properties import QuickSightJoinOperandProperties
from .quick_sight_transform_operation_source import QuickSightTransformOperationSource


class QuickSightJoinOperation(BaseModel):
    Alias: StrictStr | None = None
    LeftOperand: QuickSightTransformOperationSource | None = None
    RightOperand: QuickSightTransformOperationSource | None = None
    Type: StrictStr | None = None
    OnClause: StrictStr | None = None
    LeftOperandProperties: QuickSightJoinOperandProperties | None = None
    RightOperandProperties: QuickSightJoinOperandProperties | None = None
