"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import ordertype as shared_ordertype
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from speakeasybar import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrderInput:
    r"""An order for a drink or ingredient."""
    product_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productCode') }})
    r"""The product code of the drink or ingredient."""
    quantity: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    r"""The number of units of the drink or ingredient to order."""
    type: shared_ordertype.OrderType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of order."""
    


class OrderStatus(str, Enum):
    r"""The status of the order."""
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETE = 'complete'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Order:
    r"""An order for a drink or ingredient."""
    product_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('productCode') }})
    r"""The product code of the drink or ingredient."""
    quantity: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    r"""The number of units of the drink or ingredient to order."""
    status: OrderStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The status of the order."""
    type: shared_ordertype.OrderType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of order."""
    
