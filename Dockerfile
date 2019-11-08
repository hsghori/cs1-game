FROM nikolaik/python-nodejs:python3.7-nodejs11
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
COPY package.json /app/
COPY package-lock.json /app/
RUN pip install -r requirements.txt
RUN npm ci
COPY . /app/
