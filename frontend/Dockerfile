FROM node:lts-alpine
WORKDIR /app
COPY package*.json ./


RUN npm install
COPY . .
RUN npm install axios --save

CMD ["npm", "run", "dev", "--", "--host"]
