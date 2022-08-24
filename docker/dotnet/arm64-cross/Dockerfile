FROM mcr.microsoft.com/dotnet-buildtools/prereqs:ubuntu-16.04-cross-arm64-20210719121212-8a8d3be AS build
WORKDIR /dotnet
ENV PATH="${PATH}:/dotnet"
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
RUN wget -q https://download.visualstudio.microsoft.com/download/pr/aabf15d3-f201-4a6c-9a7e-def050d054af/0a8eba2d8abcf1c28605744f3a48252f/dotnet-sdk-7.0.100-preview.7.22377.5-linux-x64.tar.gz && \
    tar -xvzf dotnet-sdk-7.0.100-preview.7.22377.5-linux-x64.tar.gz && \
    rm -rf dotnet-sdk-7.0.100-preview.7.22377.5-linux-x64.tar.gz
