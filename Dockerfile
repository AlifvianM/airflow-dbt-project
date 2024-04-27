FROM apache/airflow:2.8.3
# USER root
# RUN apt-get update \
#   && apt-get install -y --no-install-recommends \
#          build-essential my-awesome-apt-dependency-to-add \
#   && apt-get autoremove -yqq --purge \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*
# USER airflow
COPY requirements.txt .
# RUN pip install --no-cache-dir --user -r requirements.txt
RUN pip install -r requirements.txt