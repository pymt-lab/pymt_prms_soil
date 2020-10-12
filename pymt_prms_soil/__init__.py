#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_prms_soil").version


from .bmi import PRMSSoil

__all__ = [
    "PRMSSoil",
]
