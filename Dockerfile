FROM apache/airflow:2.5.1-python3.9

USER root

# Install git
RUN apt-get update && apt-get install -y \
    git \
    wget

# Clone the GitHub repo with Airflow DAGs
ARG DAGS_REPO=https://github.com/omkar-kapase/airflow.git
ARG DAGS_BRANCH=main

RUN git clone --branch ${DAGS_BRANCH} ${DAGS_REPO} /usr/local/airflow/dags

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

USER airflow
ENTRYPOINT ["/bin/bash", "/start.sh"]


# FROM apache/airflow:2.5.1-python3.9

# COPY requirements.txt /requirements.txt

# RUN pip install --no-cache-dir -r /requirements.txt

# USER root

# RUN apt-get update && apt-get install -y \
#     wget

# COPY start.sh /start.sh
# RUN chmod +x /start.sh
# USER airflow
# ENTRYPOINT ["/bin/bash","/start.sh"]
