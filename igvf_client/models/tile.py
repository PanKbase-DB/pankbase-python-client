# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 48.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Tile(BaseModel):
    """
    The coordinates and an identifier in plain text for the specific tile of a protein region cloned in an expression vector library. The associated gene for this protein must be listed in the small_scale_gene_list or large_scale_gene_list property.
    """ # noqa: E501
    tile_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="An identifier in plain text for the specific tile of a protein region cloned in an expression vector library.")
    tile_start: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The 1-based, closed (inclusive) starting coordinate.")
    tile_end: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The 1-based, closed (inclusive) ending coordinate.")
    __properties: ClassVar[List[str]] = ["tile_id", "tile_start", "tile_end"]

    @field_validator('tile_id')
    def tile_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\S+(\s|\S)*\S+|\S)$", value):
            raise ValueError(r"must validate the regular expression /^(\S+(\s|\S)*\S+|\S)$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Tile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Tile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tile_id": obj.get("tile_id"),
            "tile_start": obj.get("tile_start"),
            "tile_end": obj.get("tile_end")
        })
        return _obj


