# py-device-properties

This application will demonstrate Azure IoT hub message properties 


## requirements
python 3
pip 
bash 

## setup steps 
### create a python virtual environment (one time)
This step will create a virtual environment in the local directorty called .venv
```bash
python -m venv .venv
```

### Source the virtual environment (every time you need the environment)
To source virtual environment
``` bash
source .venv/bin/activate
```
This past step will add path to the virtual environment. You can deactivate with the following command: 
```bash
deactivate 
```

### Install requirements - after you have sourced environment (one time)
```bash 
pip install -r requirements.txt
```

### Rename env_set_example to env_set.sh (one time). Copy SAS token to this file(one time). Source this file (each time you need the environment )
There is an example env set script provided: env_set_example, rename this file to env_set.sh ( this is ignored by git). Source this file: 
```
source ./env_set.sh
```
