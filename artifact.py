import comet_ml
import os
from comet_ml import Artifact, API
import random
import string
import time
import comet_ml
from comet_ml import Artifact, Experiment, API

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

project_name = 'random_' + new_random_string

SomeArtifact = comet_ml.Artifact(name="artifact_" + random_string)

# # First experiment to produce artifact
experiment = comet_ml.Experiment(workspace="ethical-buck-8476", project_name=project_name)
experiment.set_name('experiment_' + random_string)
SomeArtifact.add('/Users/mikam/Desktop/newScripts/log.txt')
experiment.log_artifact(SomeArtifact)
experiment.end()

# Second experiment to consume the artifact from the previews experiment
experiment = comet_ml.Experiment(workspace="ethical-buck-8476", project_name=project_name)
time.sleep(10)
experiment.get_artifact("artifact_" + random_string)

# add model

# experiment = Experiment(workspace="ethical-buck-8476", project_name=project_name)
# experiment.log_model('bbb', '/Users/mikam/Desktop/Scripts/date.py')
# experiment.register_model('bbb', version="1.77.369")