FROM node:lts-alpine

WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm install
CMD ["npm", "run", "dev", "--", "--host"]

EXPOSE 5173