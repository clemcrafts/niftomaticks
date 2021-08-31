# Niftomaticks
An application to back collectible investments with data.

![alt tag](https://i.ibb.co/p0ZKMtn/Screenshot-2021-08-30-at-18-36-25.png)


## Launch the job

Install the requirements:

```
virutalenv env -p python3.8
source env/bin/activate
pip install -r requirements.txt 
```

To fetch the data:

```
python fetch.py
```

A CSV with a subscribers count will be generated.

To plot the data:

```
python plot.py
```
