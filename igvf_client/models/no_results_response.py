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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from igvf_client.models.no_results_response_columns_value import NoResultsResponseColumnsValue
from igvf_client.models.no_results_response_facet_groups_inner import NoResultsResponseFacetGroupsInner
from igvf_client.models.no_results_response_facets_inner import NoResultsResponseFacetsInner
from igvf_client.models.no_results_response_filters_inner import NoResultsResponseFiltersInner
from igvf_client.models.no_results_response_sort_value import NoResultsResponseSortValue
from typing import Optional, Set
from typing_extensions import Self

class NoResultsResponse(BaseModel):
    """
    NoResultsResponse
    """ # noqa: E501
    context: Optional[StrictStr] = Field(default=None, alias="@context")
    graph: Optional[List[Any]] = Field(default=None, alias="@graph")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[List[StrictStr]] = Field(default=None, alias="@type")
    clear_filters: Optional[StrictStr] = None
    columns: Optional[Dict[str, NoResultsResponseColumnsValue]] = None
    facet_groups: Optional[List[NoResultsResponseFacetGroupsInner]] = None
    facets: Optional[List[NoResultsResponseFacetsInner]] = None
    filters: Optional[List[NoResultsResponseFiltersInner]] = None
    notification: Optional[StrictStr] = None
    sort: Optional[Dict[str, NoResultsResponseSortValue]] = None
    title: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["@context", "@graph", "@id", "@type", "clear_filters", "columns", "facet_groups", "facets", "filters", "notification", "sort", "title", "total"]

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
        """Create an instance of NoResultsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in columns (dict)
        _field_dict = {}
        if self.columns:
            for _key in self.columns:
                if self.columns[_key]:
                    _field_dict[_key] = self.columns[_key].to_dict()
            _dict['columns'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in facet_groups (list)
        _items = []
        if self.facet_groups:
            for _item in self.facet_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['facet_groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in facets (list)
        _items = []
        if self.facets:
            for _item in self.facets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['facets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in sort (dict)
        _field_dict = {}
        if self.sort:
            for _key in self.sort:
                if self.sort[_key]:
                    _field_dict[_key] = self.sort[_key].to_dict()
            _dict['sort'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NoResultsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": obj.get("@context"),
            "@graph": obj.get("@graph"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "clear_filters": obj.get("clear_filters"),
            "columns": dict(
                (_k, NoResultsResponseColumnsValue.from_dict(_v))
                for _k, _v in obj["columns"].items()
            )
            if obj.get("columns") is not None
            else None,
            "facet_groups": [NoResultsResponseFacetGroupsInner.from_dict(_item) for _item in obj["facet_groups"]] if obj.get("facet_groups") is not None else None,
            "facets": [NoResultsResponseFacetsInner.from_dict(_item) for _item in obj["facets"]] if obj.get("facets") is not None else None,
            "filters": [NoResultsResponseFiltersInner.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "notification": obj.get("notification"),
            "sort": dict(
                (_k, NoResultsResponseSortValue.from_dict(_v))
                for _k, _v in obj["sort"].items()
            )
            if obj.get("sort") is not None
            else None,
            "title": obj.get("title"),
            "total": obj.get("total")
        })
        return _obj


