# Network Analysis with Batfish
This is a live project repository supporting the blogseries at Karneliuk.com

## Usage
You can read the details in [out blog about it](https://karneliuk.com).
In a nutshell, the steps are:
1. Make sure your Docker is up and running checking with `docker info`.
2. Download the Batfish container `docker image pull batfish/allinone`.
3. Launch it `docker run -d --name batfish -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone`.
4. Create the Python virtual environment `python3.9 -m venv venv`.
5. Activate it `source venv/bin/activate`.
6. Install requirements `pip install -r requirements.txt`.
7. Launch the Python script `python main.py` with provided lab files.

# Our Services
## Are You Interested to Implement Batfish in Your Company?
Our consulting services are at your disposal. [Get in touch with us](mailto:training@karneliuk.com).

## Do You Want to Be Automation Professional?
[Join our Zero-to-Hero Network Automation Training](http://bit.ly/2mP3SJy)

(c)2021, Karneliuk.com