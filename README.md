# magicdirheadless
A directory finder made in python with a few features like multi-threading and 3 different methods of directory existence verification this version contains a headless browser for extra verification. 

# Setup

## Install required modules before use

```
pip install requests
```
```
pip install beautifulsoup4
```
```
pip install tqdm
```
```
pip install selenium
```
## Create or locate a directory list

Example (list.txt)
```
home
about
contact
login
signup
ect...
```

# Usage

```
cd magicdirheadless
```
```
python3 magicdirheadless.py
```

The rest is pretty straightforward just input the correct information when asked and you will be fine. When asked for a thread count you may type 1 for default or specify a number of threade that works best with your system specifications. For this version using the headless browser I do not reccomend using any more threads that cores for your system. If you have 2 cores on your machine use 2 threads max!
