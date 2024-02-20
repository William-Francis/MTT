# Getting started
```sh 
cp .env.example .env
docker compose -f docker-compose.debug.yml build
docker compose -f docker-compose.debug.yml run vite pnpm install
docker compose -f docker-compose.debug.yml up
 ```

 Then visit localhost

 