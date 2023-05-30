FROM node

WORKDIR /app

RUN npm install -g @angular/cli@14

COPY . .

RUN npm install

CMD ["ng", "serve", "--host", "0.0.0.0", "--disable-host-check"]
