# DevOps Assignment 2 - Adil Javed

**Roll number:** FA23-BAI-006

A compact HTML/CSS edition of my existing AI and Data Science portfolio:
https://khan68-max.github.io/portfolio/

The assignment edition uses a dark theme with cyan and blue accents, adds
my roll number, and is served by nginx inside Docker. GitHub Actions validates
the page and builds the image on pull requests. Pushes to main also publish
the latest image to Docker Hub.

## Local validation

Create and activate a Python virtual environment, then run:

```powershell
python check_page.py
```

The checker uses Python's standard library. No pip packages are needed.

## Docker in GitHub Codespaces

Run the Docker commands in the GitHub Codespaces terminal.
Replace YOUR_DOCKERHUB_USERNAME with your actual Docker Hub username.

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/devops-a2:manual .
docker run -d -p 8080:80 --name page YOUR_DOCKERHUB_USERNAME/devops-a2:manual
```

Use Codespaces Ports > 8080 > Open in Browser to view the container.

## GitHub Actions secrets

- DOCKERHUB_USERNAME: Docker Hub username.
- DOCKERHUB_TOKEN: Docker Hub personal access token with write access.

For a roll number ending in 6, the required extra section is Labs.
Add this section on feature-endpoint and merge it using a pull request.
