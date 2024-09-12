# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 49.0.1
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

class Locus1(BaseModel):
    """
    Locus1
    """ # noqa: E501
    assembly: StrictStr = Field(description="The genome assembly to which coordinates relate (e.g., GRCh38).")
    chromosome: Annotated[str, Field(strict=True)] = Field(description="The number (or letter) designation for the chromosome, e.g. chr1 or chrX")
    start: Annotated[int, Field(strict=True, ge=1)] = Field(description="The 1-based, closed (inclusive) starting coordinate.")
    end: Annotated[int, Field(strict=True, ge=1)] = Field(description="The 1-based, closed (inclusive) ending coordinate.")
    __properties: ClassVar[List[str]] = ["assembly", "chromosome", "start", "end"]

    @field_validator('assembly')
    def assembly_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['GRCh38', 'GRCm39']):
            raise ValueError("must be one of enum values ('GRCh38', 'GRCm39')")
        return value

    @field_validator('chromosome')
    def chromosome_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(chr[0-9A-Za-z_]+)$", value):
            raise ValueError(r"must validate the regular expression /^(chr[0-9A-Za-z_]+)$/")
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
        """Create an instance of Locus1 from a JSON string"""
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
        """Create an instance of Locus1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assembly": obj.get("assembly"),
            "chromosome": obj.get("chromosome"),
            "start": obj.get("start"),
            "end": obj.get("end")
        })
        return _obj


