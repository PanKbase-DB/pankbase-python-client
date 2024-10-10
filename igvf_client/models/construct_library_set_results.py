# coding: utf-8

"""
    IGVF Project API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 52.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from igvf_client.models.construct_library_set import ConstructLibrarySet
from igvf_client.models.search_facet import SearchFacet
from typing import Optional, Set
from typing_extensions import Self

class ConstructLibrarySetResults(BaseModel):
    """
    ConstructLibrarySetResults
    """ # noqa: E501
    graph: Optional[List[ConstructLibrarySet]] = Field(default=None, alias="@graph")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    total: Optional[StrictInt] = None
    facets: Optional[List[SearchFacet]] = None
    __properties: ClassVar[List[str]] = ["@graph", "@id", "@type", "total", "facets"]

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
        """Create an instance of ConstructLibrarySetResults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in graph (list)
        _items = []
        if self.graph:
            for _item in self.graph:
                if _item:
                    _items.append(_item.to_dict())
            _dict['@graph'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in facets (list)
        _items = []
        if self.facets:
            for _item in self.facets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['facets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConstructLibrarySetResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@graph": [ConstructLibrarySet.from_dict(_item) for _item in obj["@graph"]] if obj.get("@graph") is not None else None,
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "total": obj.get("total"),
            "facets": [SearchFacet.from_dict(_item) for _item in obj["facets"]] if obj.get("facets") is not None else None
        })
        return _obj


