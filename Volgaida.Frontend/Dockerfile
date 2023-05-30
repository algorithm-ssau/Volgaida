FROM node

WORKDIR /app

RUN npm install -g @angular/cli@14

RUN npm install -g @angular-devkit/build-angular@14.2.11

RUN npm cache clean --force

COPY . .

RUN npm install

RUN npm run build --prod


FROM nginx:latest AS ngi

COPY --from=build /dist/src/app/dist/my-docker-angular-app /usr/share/nginx/html
COPY /nginx.conf  /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
