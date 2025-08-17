# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install any needed packages
RUN npm install

# Copy the rest of the application's code
COPY . .

# The command to run the application is specified in docker-compose.yml
# But we can add a default command here as well
EXPOSE 3000
CMD ["npm", "run", "dev"]
