from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_categorical_dimension_field import QuickSightCategoricalDimensionField
from .quick_sight_date_dimension_field import QuickSightDateDimensionField
from .quick_sight_numerical_dimension_field import QuickSightNumericalDimensionField


class QuickSightDimensionField(BaseModel):
    NumericalDimensionField: QuickSightNumericalDimensionField | None = None
    CategoricalDimensionField: QuickSightCategoricalDimensionField | None = None
    DateDimensionField: QuickSightDateDimensionField | None = None
