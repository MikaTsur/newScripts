import comet_ml
import os
from comet_ml import Artifact, API
import random
import string
import time

os.environ["COMET_AUTO_LOG_GIT_METADATA"] = "false"
os.environ['COMET_AUTO_LOG_GIT_PATCH'] = "false"
os.environ['COMET_URL_OVERRIDE'] = 'https://staging.dev.comet.com/clientlib/'
os.environ['COMET_OPTIMIZER_URL'] = 'https://staging.dev.comet.com/optimizer/'
os.environ["COMET_API_KEY"] = "gKw3yV5sAcGsJUxiKAVgXQrdo"


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


new_random_string = generate_random_string()

random_string = 'random_' + new_random_string

# First experiment to produce artifact
experiment = comet_ml.Experiment(workspace="mikam1", project_name='project_' + random_string)
experiment.set_name('experiment_' + random_string)
SomeArtifact = comet_ml.Artifact(name="artifact_" + random_string)
SomeArtifact.add('/Users/mikam/Desktop/newScripts/log.txt')
experiment.log_artifact(SomeArtifact)

# Second experiment to consume the artifact from the previews experiment
experiment = comet_ml.Experiment(workspace="mikam1", project_name='project_' + random_string)
time.sleep(10)
experiment.get_artifact("artifact_" + random_string)
