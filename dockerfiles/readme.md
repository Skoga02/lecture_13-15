

To enter a docker container (perfect for debugging)
* enter terminal and type docker ps
* copy the container id
* command: docker exec it _container-id_ bash
* example command: cat _api.py_ (concatinate api.py)

* command: uv pip freeze -- shows enviroment dependencies

# jump in to an existing running container
docker exec -it container_name bash

# if container is dead - spin up a new one interactively
docker run -it image_name bash