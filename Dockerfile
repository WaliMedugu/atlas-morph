# ==============================================================================
# ATLAS-MORPH: Sovereign Inference Acceleration Suite Dockerfile
# Based on NeurIPS 2023 LLM Efficiency Challenge 1st-Place Submission Standards
# ==============================================================================

FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    PORT=7860

WORKDIR /app

# Install system utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy package requirements and files
COPY setup.py pyproject.toml README.md /app/
COPY atlas_morph/ /app/atlas_morph/
COPY web_dashboard/ /app/web_dashboard/
COPY app.py /app/

# Install atlas-morph
RUN pip install --no-cache-dir -e .

EXPOSE 7860 8000

# Launch server
CMD ["python", "app.py"]
