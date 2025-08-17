# --- Build Stage ---
FROM node:18 AS build

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# --- Production Stage ---
FROM node:18-alpine

WORKDIR /usr/src/app

ENV NODE_ENV=production

# Copy built artifacts from the build stage
COPY --from=build /usr/src/app/.output ./.output
COPY --from=build /usr/src/app/node_modules ./node_modules
COPY package.json .

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]
