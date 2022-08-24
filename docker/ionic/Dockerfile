FROM chaldea/jdk-node:16
ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG NODEJS_VERSION="16"
ARG ANDROID_SDK_VERSION="8512546"
ARG ANDROID_HOME="/opt/android-sdk"
ARG ANDROID_BUILD_TOOLS_VERSION="33.0.0"

ENV ANDROID_HOME "${ANDROID_HOME}"

# 安装ionic
RUN npm install -g @ionic/cli

# 安装android sdk
RUN cd /tmp \
    && curl --proxy ${HTTP_PROXY} -fSLk https://dl.google.com/android/repository/commandlinetools-linux-${ANDROID_SDK_VERSION}_latest.zip -o sdk-tools-linux-${ANDROID_SDK_VERSION}.zip \
    && unzip sdk-tools-linux-${ANDROID_SDK_VERSION}.zip \
    && mkdir -p /opt/android-sdk/cmdline-tools \
    && mv cmdline-tools /opt/android-sdk/cmdline-tools/latest \
    && (while sleep 3; do echo "y"; done) | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses \
    && $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager "platform-tools" \
    && $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
    && apt-get autoremove -y \
    && rm -rf /tmp/sdk-tools-linux-${ANDROID_SDK_VERSION}.zip \ 
    && mkdir /ionicapp

# 安装MC
RUN curl --proxy ${HTTP_PROXY} -fSLk https://dl.min.io/client/mc/release/linux-amd64/mc -o /usr/local/bin/mc && \
    chmod +x /usr/local/bin/mc

WORKDIR /ionicapp