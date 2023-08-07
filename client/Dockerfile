FROM --platform=$BUILDPLATFORM node:18.16-alpine AS development

WORKDIR /app

COPY . /app

RUN yarn

CMD ["yarn", "dev"]
