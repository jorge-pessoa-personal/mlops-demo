import os
import neptune.new as neptune
import uuid

HASH = uuid.uuid4().hex[:5]

neptune.init_model(
    name=f"production-model-{HASH}",
    project="jpessoa/demo", 
    key=f"PROD_{HASH}",
    api_token=os.environ["NEPTUNE_API_KEY"]
)

model = neptune.init_model_version(
    model="DEM-PROD_{HASH}",
    project="jpessoa/demo", 
    api_token=os.environ["NEPTUNE_API_KEY"]
)

model["pickled"].upload("models/model.pkl")
model.change_stage("production")
