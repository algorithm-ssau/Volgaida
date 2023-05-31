FROM node:latest as builder

WORKDIR /app

COPY ./package.json ./

RUN npm i

COPY . .

#RUN npm install -g @angular/cli@14

#RUN npm install -g @angular-devkit/build-angular@14.2.11

#CMD ["npm", "run", "start"]

RUN npm run build

FROM nginx:latest
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/dist/volgaida.frontend /usr/share/nginx/html

#EXPOSE 4200:80

#CMD ["nginx", "-g", "daemon off;"]
