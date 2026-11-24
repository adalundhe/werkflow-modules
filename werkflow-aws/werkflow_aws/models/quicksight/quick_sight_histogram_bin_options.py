from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .quick_sight_bin_count_options import QuickSightBinCountOptions
from .quick_sight_bin_width_options import QuickSightBinWidthOptions


class QuickSightHistogramBinOptions(BaseModel):
    SelectedBinType: StrictStr | None = None
    BinCount: QuickSightBinCountOptions | None = None
    BinWidth: QuickSightBinWidthOptions | None = None
    StartValue: StrictFloat | StrictInt | None = None
