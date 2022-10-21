from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
# from __seedwork.domain.entities import Entity
# from __seedwork.domain.exceptions import EntityValidationException

#kw_only ->
#frozen  ->
#slots   ->
@dataclass(kw_only=True, frozen=True, slots=True)  # init, repr, eq
class Category:

    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=datetime.now
    )