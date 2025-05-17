from fastapi import FastAPI
import logging

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

trace.set_tracer_provider(TracerProvider())
#otlp_exporter = OTLPSpanExporter(endpoint="http://otelcol:4318/v1/traces", insecure=True)
otlp_exporter = OTLPSpanExporter(endpoint="http://otelcol:4318/v1/traces")
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))
FastAPIInstrumentor.instrument_app(app)

logger = logging.getLogger("uvicorn")

@app.get("/")
async def root():
    logger.info("Test log from FastAPI")
    return {"message": "Hello, logs!"}
