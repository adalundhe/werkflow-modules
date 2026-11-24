from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_date_array_options import CloudSearchDateArrayOptions
from .cloud_search_date_options import CloudSearchDateOptions
from .cloud_search_double_array_options import CloudSearchDoubleArrayOptions
from .cloud_search_double_options import CloudSearchDoubleOptions
from .cloud_search_int_array_options import CloudSearchIntArrayOptions
from .cloud_search_int_options import CloudSearchIntOptions
from .cloud_search_lat_lon_options import CloudSearchLatLonOptions
from .cloud_search_literal_array_options import CloudSearchLiteralArrayOptions
from .cloud_search_literal_options import CloudSearchLiteralOptions
from .cloud_search_text_array_options import CloudSearchTextArrayOptions
from .cloud_search_text_options import CloudSearchTextOptions


class CloudSearchIndexField(BaseModel):
    IndexFieldName: StrictStr | None = None
    IndexFieldType: StrictStr | None = None
    IntOptions: CloudSearchIntOptions | None = None
    DoubleOptions: CloudSearchDoubleOptions | None = None
    LiteralOptions: CloudSearchLiteralOptions | None = None
    TextOptions: CloudSearchTextOptions | None = None
    DateOptions: CloudSearchDateOptions | None = None
    LatLonOptions: CloudSearchLatLonOptions | None = None
    IntArrayOptions: CloudSearchIntArrayOptions | None = None
    DoubleArrayOptions: CloudSearchDoubleArrayOptions | None = None
    LiteralArrayOptions: CloudSearchLiteralArrayOptions | None = None
    TextArrayOptions: CloudSearchTextArrayOptions | None = None
    DateArrayOptions: CloudSearchDateArrayOptions | None = None
