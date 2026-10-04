# Centralizes runtime configuration for the LLM model and generation parameters.

import os

LLM_MODEL = os.getenv("LLM_MODEL", "gemma3:4b")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.2"))