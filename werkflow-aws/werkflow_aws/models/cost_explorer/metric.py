from pydantic import BaseModel, StrictStr
from .amount import Amount


class Metric(BaseModel):
    Amount: Amount
    Unit: StrictStr

    def model_dump(self, *, mode = 'python', include = None, exclude = None, context = None, by_alias = None, exclude_unset = False, exclude_defaults = False, exclude_none = False, round_trip = False, warnings = True, fallback = None, serialize_as_any = False):
        dumped = super().model_dump(mode=mode, include=include, exclude=exclude, context=context, by_alias=by_alias, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none, round_trip=round_trip, warnings=warnings, fallback=fallback, serialize_as_any=serialize_as_any)
        dumped['Amount'] = str(dumped['Amount'])
        
        return dumped