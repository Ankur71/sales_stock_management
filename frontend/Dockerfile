# frontend/Dockerfile
FROM node:16

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Copy project files
COPY . .

# Build the Vue.js application
RUN npm run build

# Serve the app using a simple server (like serve)
RUN npm install -g serve
CMD ["serve", "-s", "dist"]
