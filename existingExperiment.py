import os

import comet_ml
from comet_ml import ExistingExperiment
os.environ['COMET_URL_OVERRIDE']='https://staging.dev.comet.com/clientlib/'
os.environ['COMET_OPTIMIZER_URL']='https://staging.dev.comet.com/optimizer/'


os.environ['COMET_URL_OVERRIDE'] = 'https://staging.dev.comet.com/clientlib/'
os.environ['COMET_OPTIMIZER_URL'] = 'https://staging.dev.comet.com/optimizer/'
os.environ['COMET_AUTO_LOG_GIT_METADATA'] = 'false'
os.environ['COMET_AUTO_LOG_GIT_PATCH'] = 'false'
os.environ["COMET_API_KEY"] = "gKw3yV5sAcGsJUxiKAVgXQrdo"
from comet_ml import API

comet_ml.init(anonymous=True)


##with this script you can edit an existing experiment e.g. add metric
##Plesae change envirnment/apiKry etc.

#os.environ["COMET_API_KEY"] = 'FRNJT6xxxr1XbUxmqIerqWuMR'

exp = ExistingExperiment(previous_experiment='88a3f82786cd41049433cc0dbfadcebb')
exp.log_metric("metric5", 5)

