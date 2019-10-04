# docker run \
#     --cap-add=SYS_ADMIN \
#     --init \
#     --rm \
#     -v /dev/shm:/dev/shm \
#     -v $(pwd):/app \
#     digitalmarketplace/bdd-tests
FROM debian:stable

ARG GAUGE_VERSION=1.0.6
ARG GAUGE_PYTHON_VERSION=0.3.6.nightly-2019-08-28

ARG USER=user
ARG USER_UID=2000

RUN apt-get update && apt-get install -y \
		curl \
		git \
		gnupg \
		python3 \
		python3-pip \
		unzip \
	&& rm -rf /var/lib/apt/lists/*

RUN curl -s https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
	&& apt-get update \
	&& apt-get install -y google-chrome-stable \
	&& rm -rf /var/lib/apt/lists/*

RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` \
	&& curl -O http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
	&& unzip chromedriver_linux64.zip -d /usr/local/bin \
	&& rm chromedriver_linux64.zip \
	&& chmod +x /usr/local/bin/chromedriver

RUN groupadd -r $USER && useradd -r -u $USER_UID -g $USER $USER \
	&& mkdir -p /home/$USER \
	&& chown -R $USER:$USER /home/$USER

RUN mkdir -p /gauge && chown -R $USER:$USER /gauge
ENV GAUGE_HOME /gauge

RUN curl -LO https://github.com/getgauge/gauge/releases/download/v$GAUGE_VERSION/gauge-$GAUGE_VERSION-linux.x86_64.zip \
	&& unzip gauge-$GAUGE_VERSION-linux.x86_64.zip -d /usr/local/bin \
	&& rm gauge-$GAUGE_VERSION-linux.x86_64.zip \
	&& chmod +x /usr/local/bin/gauge \
	&& gauge telemetry off \
	&& chown -R $USER:$USER /gauge

# RUN gauge install python -v $GAUGE_PYTHON_VERSION
# Install nightly build of gauge python plugin, it has fixes we need
RUN curl -L https://bintray.com/gauge/gauge-python/download_file?file_path=gauge-python-$GAUGE_PYTHON_VERSION.zip \
		> gauge-python-$GAUGE_PYTHON_VERSION.zip \
	&& gauge install python -f gauge-python-$GAUGE_PYTHON_VERSION.zip \
	&& rm gauge-python-$GAUGE_PYTHON_VERSION.zip

RUN mkdir -p /app && chown -R $USER:$USER /app
WORKDIR /app

COPY constraints.txt requirements.txt manifest.json ./
COPY env ./

RUN pip3 install --no-cache-dir -r requirements.txt -c constraints.txt \
	&& gauge install

USER user

CMD ["gauge", "run"]
