"""Template object
This file defines the 'Template' object
The Template object is a base for a 'Paper' object, as well as any objects used as part of a Paper 
object, and is defined on startup by parsing each file in `/data/core-assets/templates`
"""
from __future__ import annotations

import logging
import yaml

from typing import Any, Callable, Dict

LOGGER = logging.getLogger(__file__)


class Template:
    """Template object to be used by Paper objects as definitions of data collection structures"""

    def __init__(self: Template) -> None:
        pass

    def _parse_template_file_to_dict(
        self: Template, template_fpath: str
    ) -> Dict[str, Any]:
        pass

    def _compute_fields(
        self: Template, template_dict: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Recursively compute fields as necessary"""
        pass

    def _compute_reference_field(
        self: Template, template_dict: Dict[str, Any], field_key: str, field_val: str
    ) -> Dict[str, Any]:
        pass

    def _compute_arithmetic_field(
        self: Template, template_dict: Dict[str, Any], field_key: str, field_val: str
    ) -> Dict[str, Any]:
        pass

    def _compute_function_field(
        self: Template, template_dict: Dict[str, Any], field_key: str, field_val: str
    ) -> Dict[str, Any]:
        pass

    def parse_sub_template(
        self: Template, subtemp_key: str, subtemp_obj: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Used to recursively parse and fill in templated objects nested in a larger template"""
        pass

    def create_callable_from_entry(
        self: Template, clickable_field: Dict[str, Any]
    ) -> Callable:
        """Used to generate a callable object given a field containing an on_call rule"""
        pass
