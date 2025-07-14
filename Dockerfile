FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    wget \
    curl \
    python3 \
    python3-pip

# Copy script
COPY stream.py /app/stream.py

WORKDIR /app

# Default command
ENTRYPOINT ["python3", "stream.py"]
