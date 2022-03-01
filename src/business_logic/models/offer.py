import typing
from datetime import datetime
from decimal import Decimal

from ._base import Model


class Offer(typing.NamedTuple):
    id: int
    value: Decimal
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime


model_offer = Model(Offer)
