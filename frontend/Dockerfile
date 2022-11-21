FROM node:lts-alpine
WORKDIR /app
COPY package*.json ./


RUN npm install
COPY . .
RUN npm install --save axios

CMD ["npm", "run", "dev", "--", "--host"]
