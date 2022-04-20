import os
import neptune.new as neptune

neptune.init_model(
    name="production-model",
    project="jpessoa/demo", 
    key="PROD",
    api_token=os.environ["NEPTUNE_API_KEY"]
)

model = neptune.init_model_version(
    model="DEM-PROD",
    project="jpessoa/demo", 
    api_token=os.environ["NEPTUNE_API_KEY"]
)

model["pickled"].upload("models/model.pkl")
model.change_stage("production")