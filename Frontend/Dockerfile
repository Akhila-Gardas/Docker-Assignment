# Start from an official Node.js setup image
FROM node:18

# Set up a workspace folder inside the box
WORKDIR /app

# Copy configuration files and install Express
COPY package*.json ./
RUN npm install

# Copy all our web layout files into the box
COPY . .

# Expose port 3000 to view in browser
EXPOSE 3000

# Command to turn on our Node server
CMD ["node", "server.js"]