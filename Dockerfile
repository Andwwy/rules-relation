# Edge inspector — pure Python stdlib, no dependencies to install.
FROM python:3.12-slim

WORKDIR /app

# Copy the vault (rule projects) + the inspector app. The vault is included so
# build_data.py can regenerate data/ inside the image if desired.
COPY . /app

# Rebuild the data from the vault at image-build time so data/ is always fresh.
RUN python3 inspector/build_data.py

WORKDIR /app/inspector

# Listen on all interfaces inside the container so the published port works.
ENV HOST=0.0.0.0
ENV PORT=7077
EXPOSE 7077

# Simple healthcheck so the orchestrator/restart policy can tell it's alive.
HEALTHCHECK --interval=30s --timeout=4s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:7077/api/projects')" || exit 1

CMD ["python3", "server.py"]
