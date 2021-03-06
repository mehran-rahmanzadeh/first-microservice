FROM python:3.9-slim

# Sync variables from docker-compose.yml (args)
# NOTE: Set GID & UID Variables if container need a non-root user container
ARG USERNAME
ARG WORKING_DIR


# Create Environment Variable for python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# The build-essential contains a collection of meta-packages that are necessary to compile software
RUN apt-get update && apt-get install -y --no-install-recommends \
            build-essential \
            libpq-dev \
            && rm -rf /var/lib/apt/lists/*


# Change project directory
WORKDIR ${WORKING_DIR}

###################### START COPY PORJECT ######################

##################################################
############### ROOT PERMISSION ##################
##################################################
COPY Pipfile ${WORKING_DIR}
COPY Pipfile.lock ${WORKING_DIR}


# Install Python packages without cache directory
RUN python -m pip install --no-cache-dir --upgrade pip && \
    pip install pipenv --no-cache-dir && \
    pipenv install --deploy --system --ignore-pipfile && \
    pipenv --clear && \
    rm -rf /tmp/Pipfil*

COPY . ${WORKING_DIR}

# Change User to container user entry

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh","/app/entrypoint.sh"]