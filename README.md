# 353 Final Project 
## Program manual: 
```bash
How to run code: IDE: Jupyter notebook(all .ipynb could see on web page)
For python file running: 
    python read_image.py
    
    it will automatically read the image from the image folder to make a new file called location.csv
    since we have limited storage on the repository, so we did not upload the image folder.
```
## Library you need to install(module):
```bash
pip3 install numpy
sudo apt-get install python3 python3-dev python3-pip
pip3 install --user scipy matplotlib pandas statsmodels scikit-learn jupyter
pip install seaborn
pip install plotly
pip3 install --user pykalman
```
## Code functionality introduction:

```bash
read_image.py:             Read the image and save the geometric information in the path.csv file 
airbnb_data.ipynb:         Handle airbnb data set combined with interesting_amenities.csv 
food_chain.ipynb:          Select the chain restaurant from osm folder 
airbnb_stats.ipynb:        Statistic analysis about the relationship between the amenity and density of airbnb
nearby_amenities.ipynb:    Filter some useful and interesting place to produce a file called interesting_amenities. csv
```