import os
import neptune.new as neptune
import uuid

model_name = f"prod-model"
model_key = "PROD"

model = neptune.init_model_version(
    model=f"MLDEMO-{model_key}",
    project="jpessoa/mlops-demo", 
    api_token=os.environ["NEPTUNE_API_KEY"]
)

model["pickled"].upload("models/model.pkl")
model.change_stage("production")
