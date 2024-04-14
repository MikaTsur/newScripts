import os
import random
import string
import comet_ml
from comet_ml import ExistingExperiment

os.environ["COMET_AUTO_LOG_GIT_METADATA"] = "false"
os.environ['COMET_AUTO_LOG_GIT_PATCH'] = "false"
#os.environ['COMET_URL_OVERRIDE'] = 'https://staging.dev.comet.com/clientlib/'
#os.environ['COMET_OPTIMIZER_URL'] = 'https://staging.dev.comet.com/optimizer/'
#os.environ["COMET_API_KEY"] = "gKw3yV5sAcGsJUxiKAVgXQrdo"
os.environ["COMET_API_KEY"] = 'FRNJT6xxxr1XbUxmqIerqWuMR'


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


new_random_string = generate_random_string()

random_string = 'random_' + new_random_string

project_name = 'random_' + new_random_string

SomeArtifact = comet_ml.Artifact(name="artifact_" + random_string)



exp = comet_ml.Experiment(project_name="25-metrics")
exp.get_artifact("artifact_random_aH9u96reBa")