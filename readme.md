## ddb_scale

### installation

  - From source
  ```
git clone https://gitlab.com/akshayo/ddb-scale
cd ddb_scale
pip3 install --user .
  ```

  - With `pip`
  ```
pip install git+http://gitlab.com/akshayo/ddb-scale
  ```

### usage

  ```
usage: ddb_scale [-h] -m CAPACITY -d {read,write} TABLE

Scale up/down any dimension of a DynamoDB table

positional arguments:
  TABLE                 name of DynamoDB table

optional arguments:
  -h, --help            show this help message and exit
  -m CAPACITY, --min-capacity CAPACITY
                        modified min capacity
  -d {read,write}, --dimension {read,write}
                        dimension to scale

  ```

### todo

 - [ ] tests
