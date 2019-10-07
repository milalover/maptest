FROM heroku/miniconda

# Grab requirements.txt.
ADD ./webapp/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

RUN conda install cython
RUN conda install cartopy
RUN conda install geopandas
RUN conda install geoplot

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
