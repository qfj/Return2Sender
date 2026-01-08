FROM python:3.11-slim
WORKDIR /app

# Copy validator, schemas, and producer folders
COPY validator validator
COPY schemas schemas
COPY producer producer

# Install dependencies
RUN pip install redis pydantic

# Run validator
CMD ["python", "-m", "validator.validator"]