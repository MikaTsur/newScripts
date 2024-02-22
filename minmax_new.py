import os
import comet_ml
import time

os.environ['COMET_URL_OVERRIDE'] = 'https://staging.dev.comet.com/clientlib/'
os.environ['COMET_OPTIMIZER_URL'] = 'https://staging.dev.comet.com/optimizer/'
os.environ['COMET_AUTO_LOG_GIT_METADATA'] = 'false'
os.environ['COMET_AUTO_LOG_GIT_PATCH'] = 'false'
os.environ["COMET_API_KEY"] = 'gKw3yV5sAcGsJUxiKAVgXQrdo'


#comet_ml.init(anonymous=True)
experiment1 = comet_ml.Experiment(project_name="for_python_panels")
experiment1.log_metric("someMetric1", 1)
experiment1.log_metric("someMetric2", 2)
experiment1.log_metric("someMetric3", 3)