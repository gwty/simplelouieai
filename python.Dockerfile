FROM continuumio/miniconda3:latest

WORKDIR /app

# Install the conda environment
COPY environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml
SHELL ["conda", "run", "--no-capture-output", "-n", "louie", "/bin/bash", "-c"]


COPY entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "louie", "./entrypoint.sh"]
