import os
import comet_ml
import time

os.environ['COMET_URL_OVERRIDE'] = 'https://staging.dev.comet.com/clientlib/'
os.environ['COMET_OPTIMIZER_URL'] = 'https://staging.dev.comet.com/optimizer/'
os.environ['COMET_AUTO_LOG_GIT_METADATA'] = 'false'
os.environ['COMET_AUTO_LOG_GIT_PATCH'] = 'false'
os.environ["COMET_API_KEY"] = 'gKw3yV5sAcGsJUxiKAVgXQrdo'


#comet_ml.init(anonymous=True)

exp = ExistingExperiment(previous_experiment='88a3f82786cd41049433cc0dbfadcebb')
exp.log_metric("metric5", 5)
