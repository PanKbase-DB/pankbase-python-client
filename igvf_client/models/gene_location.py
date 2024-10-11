# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 52.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class GeneLocation(BaseModel):
    """
    Gene location specified using 1-based, closed coordinates for a specific version of the reference genome assembly.
    """ # noqa: E501
    start: Annotated[int, Field(strict=True, ge=0)] = Field(description="The starting coordinate.")
    end: Annotated[int, Field(strict=True, ge=0)] = Field(description="The ending coordinate.")
    chromosome: Annotated[str, Field(strict=True)] = Field(description="The number (or letter) designation for the chromosome, e.g. chr1 or chrX")
    assembly: StrictStr = Field(description="The genome assembly to which coordinates relate. e.g. GRCh38.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["start", "end", "chromosome", "assembly"]

    @field_validator('chromosome')
    def chromosome_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(chr[0-9A-Za-z]+)$", value):
            raise ValueError(r"must validate the regular expression /^(chr[0-9A-Za-z]+)$/")
        return value

    @field_validator('assembly')
    def assembly_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Cast - GRCm39', 'GRCh38', 'GRCm39']):
            raise ValueError("must be one of enum values ('Cast - GRCm39', 'GRCh38', 'GRCm39')")
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
        """Create an instance of GeneLocation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GeneLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "start": obj.get("start"),
            "end": obj.get("end"),
            "chromosome": obj.get("chromosome"),
            "assembly": obj.get("assembly")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


