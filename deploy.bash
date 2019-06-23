 #!/bin/bash -e
 cat <<EOF >> ~/.pypirc
 [distutils]
 index-servers=pypi
 [pypi]
 username=${PYPI_USERNAME}
 password=${PYPI_PASSWORD}
 EOF
 python3 setup.py sdist upload;
 