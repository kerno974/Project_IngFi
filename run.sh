pip3 install virtual env
pip3 install --upgrade virtualenv
if [[ ! -d ".env"]]
then
    virtualenv -p python3 .env
fi
source .env/bin/activate
pip3 install pandas
pip3 install numpy

python3 main.py
