import multiprocessing
import time
from comet_ml import Experiment
import os

os.environ['COMET_URL_OVERRIDE'] = 'https://staging.dev.comet.com/clientlib/'
os.environ['COMET_OPTIMIZER_URL'] = 'https://staging.dev.comet.com/optimizer/'
os.environ['COMET_AUTO_LOG_GIT_METADATA'] = 'false'
os.environ['COMET_AUTO_LOG_GIT_PATCH'] = 'false'

def f():
    experiment = Experiment(api_key="gKw3yV5sAcGsJUxiKAVgXQrdo!eyJiYXNlVXJsIjoiaHR0cHM6Ly9zdGFnaW5nLmRldi5jb21ldC5jb20ifQ", auto_output_logging="simple", project_name="multiprocess_end_no_end")

    for i in range(50):
        metric_name = f"metric_{i}"
        param_name = f"param_{i}"
        log_other = f"log_other_{i}"
        experiment.log_metric(metric_name, 0.01)
        experiment.log_parameters(param_name, 1)
        time.sleep(1)
        experiment.log_other(log_other, 0.2)
    experiment.end()

if __name__ == '__main__':
    mp = multiprocessing.get_context("spawn")

    process = mp.Process(
        target=f,
        args=(),
        daemon=False,
    )

    process.start()
    process.join()
