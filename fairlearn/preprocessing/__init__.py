# Copyright (c) Microsoft Corporation and Fairlearn contributors.
# Licensed under the MIT License.

"""Preprocessing tools to help deal with sensitive attributes."""

from ._correlation_remover import CorrelationRemover
from ._optimPreproc import OptimizedPreprocessor

__all__ = ["CorrelationRemover", "OptimizedPreprocessor"]
