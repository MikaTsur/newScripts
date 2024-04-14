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
os.environ["COMET_API_KEY"] = 'FRNJT6xxxr1XbUxmqIerqWuMR'


#experiment = Experiment(workspace="ethical-buck-8476", project_name="sdk_improvment")    #creates experiment
experiment = Experiment(workspace="mikatsur")
experiment.log_model('bbb', '/Users/mikam/Desktop/Scripts/date.py')
experiment.register_model('bbb', version="1.77.369")