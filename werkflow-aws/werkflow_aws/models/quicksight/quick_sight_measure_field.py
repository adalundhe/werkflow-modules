from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_calculated_measure_field import QuickSightCalculatedMeasureField
from .quick_sight_categorical_measure_field import QuickSightCategoricalMeasureField
from .quick_sight_date_measure_field import QuickSightDateMeasureField
from .quick_sight_numerical_measure_field import QuickSightNumericalMeasureField


class QuickSightMeasureField(BaseModel):
    NumericalMeasureField: QuickSightNumericalMeasureField | None = None
    CategoricalMeasureField: QuickSightCategoricalMeasureField | None = None
    DateMeasureField: QuickSightDateMeasureField | None = None
    CalculatedMeasureField: QuickSightCalculatedMeasureField | None = None
