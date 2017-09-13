#!/bin/bash

set -ev

if [ ${TRAVIS_SECURE_ENV_VARS} = "true" ]; then
  openssl aes-256-cbc -K $encrypted_a9942967d0d9_key -iv $encrypted_a9942967d0d9_iv -in travis_access.enc -out travis_access -d;
  eval $(ssh-agent -s);
  chmod 600 travis_access && ssh-add travis_access;
  mkdir -p ~/.ssh;
  echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config;
  rsync -avz --delete output/ $DEPLOYMENT_URL;
fi

exit 0;
