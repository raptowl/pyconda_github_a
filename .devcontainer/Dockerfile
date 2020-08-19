FROM python:3.7.7

# 作業ユーザー
ARG USER_NAME

# 作業ユーザーの追加
RUN useradd -m -s /bin/bash ${USER_NAME}
# 作業ディレクトリを追加
RUN mkdir /home/${USER_NAME}/workdir \
    && chown -R ${USER_NAME}:${USER_NAME} /home/${USER_NAME}/workdir
WORKDIR /home/${USER_NAME}/workdir

# aptのアップデート、基本的なユーティリティをインストール
RUN apt-get update \
    && apt-get install -y \
        software-properties-common \
        file \
        curl \
        vim \
        git
# 必要なライブラリをインストール
# python-packages
RUN pip install \
        numpy \
        pytest \
        flake8

USER ${USER_NAME}
# dotfilesのセットアップ
ENV DOTFILES_DIR=/home/${USER_NAME}/.dotfiles
RUN (cd /home/${USER_NAME} \
     && curl -L https://raw.githubusercontent.com/raptowl/dotfiles/master/etc/setup.sh \
     | sh \
     && sh ${DOTFILES_DIR}/etc/installer/git-prompt_sh)
