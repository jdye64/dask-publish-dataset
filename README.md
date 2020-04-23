# Dask CUDA Distributed Publish Example

1. ```conda env create -f ./dask_publish_env.yml```
2. ```conda activate dask_publish```
3. Start Dask Scheduler on CLI ```dask-scheduler```
4. Start Dask Cuda Worker on CLI ```dask-cuda-worker localhost:8786```
3. Start a python process to create a publish the ddf ```python publish_client.py```
4. Start a python process to read the published ddf ```python read_client.py```

After running you can see that second Python process was able to view the contents that were
published by the first python process
