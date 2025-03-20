# docker-devops-project

## Project Overview
This project is a Docker-based DevOps setup that includes a Flask API backend, a static frontend served by Nginx, a PostgreSQL database, and Kubernetes manifests for deployment. It also incorporates GitHub Actions for CI/CD automation.

## Directory Structure
- **backend/**: Contains the Flask API implementation, including application code, routes, models, and configurations.
- **frontend/**: Holds static files (HTML, CSS, JavaScript) and Nginx configuration files for serving these assets.
- **database/**: Includes setup scripts and configurations for PostgreSQL, such as initialization scripts and connection settings.
- **k8s/**: Contains Kubernetes manifests for deploying the application, including deployment, service, and ingress configurations.
- **.github/workflows/**: Contains GitHub Actions workflows for automating testing, building, and deployment processes.
- **Dockerfile**: Defines the optimized multi-stage build process for creating the Docker image.
- **docker-compose.yml**: Specifies the multi-container setup for the application, detailing services, networks, and volumes.
- **.env**: Contains environment variables used by the application, such as database connection strings and API keys.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd docker-devops-project
   ```

2. Create a `.env` file based on the provided `.env.example` template and fill in the necessary environment variables.

3. Build and run the application using Docker Compose:
   ```
   docker-compose up --build
   ```

4. Access the application:
   - Flask API: `http://localhost:5000`
   - Frontend: `http://localhost:80`

## Usage Guidelines
- Ensure Docker and Docker Compose are installed on your machine.
- Modify the configurations in the `.env` file as needed for your environment.
- Use the provided Kubernetes manifests in the `k8s/` directory to deploy the application to a Kubernetes cluster.

## CI/CD
The project includes GitHub Actions workflows located in the `.github/workflows/` directory to automate testing and deployment processes. Ensure that your repository is connected to GitHub Actions to take advantage of these workflows.

## License
This project is licensed under the MIT License. See the LICENSE file for more details."# docker-devops-project" 
