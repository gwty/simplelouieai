# Mini Louie.AI

A starting point for dockerized python web

## Development

### Prerequisites
 - Docker
 - Docker Compose
 - Node.js


### Initialize data set

 - `./init-data.sh`

### Frontend

 - `cd frontend`
 - `npm i`
 - `npm run dev`

### Run Server on host

 - `uvicorn server.main:app --reload`

### Docker

 - `./dc build`
 - `./dc up`

To update docker python libraries, add them to environment.yml. Note `./dc` is a convience alias for `docker compose`.