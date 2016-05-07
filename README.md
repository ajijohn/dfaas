dfaas-api
===========

Official DFAAS API Wrapper.

# Installation
git clone https://github.com/ajijohn/dfaas.git dfaas

# Usage
from dfaas.api import DFAASApiClient

## DFAAS API

```python
dfaas_client = DFAASApiClient(KEY,IP)
```

### Get list of workers serving the cluster
```python
dfaasworkers = dfaas_client.poke(active="True")
```


## Submit a filtering job
```python
from dfaas.api import DFAASApiClient
dfaas_client = DFAASApiClient(KEY,IP)

#regions=1:900-1000&&subpops=CHB&format=reformat&nfs=yes
job_tracking_id = dfaas_client.spawn(regions = '1:900-1000', subpops = 'CHB', format = 'reformat',nfs='yes')
print("Tracking id " + job_tracking_id)
```

### Status
```python
dfaas_status = dfaas_client.status(tracking = job_tracking_id)
```


### Get insights into your job
```python
dfaas_insights = dfaas_client.insight(tracking = job_tracking_id,type = 'throughput')
```

### Get details of your job.
```python
job_details = dfaas_client.get_details(tracking = job_tracking_id,audit = 'True')
```




