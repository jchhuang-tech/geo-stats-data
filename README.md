# 353 Final Project 
## Program manual: 
```bash
How to run code: IDE: Jupyter notebook(all .ipynb could see on web page)
For the read_image.py file: 
    python3 read_image.py
    
    we did not upload the photos to the Git repository because they are too large(>400 MB), so the code would not run.
    but with the photos, it would automatically read the photos from the photos directory to make a new file called photos.csv
```
## Libraries/modules you need to install:
```bash
pip3 install numpy
sudo apt-get install python3 python3-dev python3-pip
pip3 install --user scipy matplotlib pandas statsmodels scikit-learn jupyter
pip install seaborn
pip install plotly
pip3 install --user pykalman
pip install exifread
```
## Code functionality introduction:

```bash
read_image.py:             Read the image and save the geometric information in the photos.csv file 
airbnb_data.ipynb:         Handle airbnb data set combined with interesting_amenities.csv 
food_chain.ipynb:          Handle the chain restaurants from osm folder 
airbnb_stats.ipynb:        Statistic analysis about the relationship between the amenity and airbnb
nearby_amenities.ipynb:    Filter some useful and interesting places and find nearby amenities
```